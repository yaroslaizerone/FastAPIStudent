from typing import List, Dict, Optional
import uuid
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage
from fa_learn_app.utils.json_repository import data_students, save_dict_to_json
from fa_learn_app.utils.repository_utils import convert_student_storage_to_out, convert_student_in_to_storage, update_student_in_storage, convert_student_dict_to_storage


class BaseStudentRepository:
    # Базовый класс для реализации функционала работы со студентами

    def get_by_id(self, id: uuid.UUID) -> StudentOut:
        raise NotImplementedError

    def get_all(self, group: str, limit: int, skip: int) -> List[StudentOut]:
        raise NotImplementedError

    def create(self, student: StudentIn) -> StudentOut:
        raise NotImplementedError

    def update_by_id(self, id: uuid.UUID, student: StudentIn) -> StudentStorage:
        raise NotImplementedError

    def delete_by_id(self, id: uuid.UUID) -> StudentOut:
        raise NotImplementedError


class StudentJsonRepository(BaseStudentRepository):
    # Реализация студента с хранилищем json

    def get_by_id(self, id: uuid.UUID) -> Optional[StudentOut]:
        # Получение студента по id

        student: StudentStorage = data_students.get(str(id))
        if student is None:
            return "Студент не найден"
        student = convert_student_dict_to_storage(student)
        student_out: StudentOut = convert_student_storage_to_out(student)
        return student_out

    def get_all(self, group: str, limit: int, skip: int) -> List[StudentOut]:
        # Получение всех студентов

        student_out_list: List[StudentOut] = []
        for _, student in data_students.items():
            if group == "":
                student = convert_student_dict_to_storage(student)
                student_out_list.append(convert_student_storage_to_out(student))
            elif student.get("group") == group:
                student = convert_student_dict_to_storage(student)
                student_out_list.append(convert_student_storage_to_out(student))
        return student_out_list[skip:skip + limit]

    def create(self, student: StudentIn) -> StudentOut:
        # Создание студента

        student_storage: StudentStorage = convert_student_in_to_storage(student)
        data_students.update({str(student_storage.id): student_storage.dict()})
        save_dict_to_json()
        student_out: StudentOut = convert_student_storage_to_out(student_storage)
        return student_out

    def update_by_id(self, id: uuid.UUID, student_new: StudentIn) -> Optional[StudentOut]:
        # Получение студента по id для обновления данных

        student_old: StudentStorage = data_students.get(str(id))
        if student_old is None:
            return "Студент не найден"

        student_update: StudentStorage = update_student_in_storage(id, student_new)
        data_students.update({str(student_update.id): student_update.dict()})
        save_dict_to_json()
        student_out: StudentOut = convert_student_storage_to_out(student_update)
        return student_out

    def delete_by_id(self, id: uuid.UUID) -> str:
        # Удаление студента по id

        student: StudentStorage = data_students.get(str(id))
        if student is None:
            return "Студент не найден"
        data_students.pop(str(id), None)
        save_dict_to_json()
        return "Студент успешно удален"
