import datetime
import uuid
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage


def convert_student_storage_to_out(student: StudentStorage) -> StudentOut:
    # Производит конвертацию StudentStorage --> StudentOut

    tmp_dict: dict = student.dict()
    tmp_dict.pop("password", None)
    return StudentOut(**tmp_dict)


def convert_student_in_to_storage(student: StudentIn) -> StudentStorage:
    # Производит конвертацию StudentIn --> StudentStorage

    tmp_dict: dict = student.dict()
    birth_date = str(tmp_dict.get('birth_date'))
    tmp_dict.update({'birth_date': birth_date})

    student_storage = StudentStorage(id=str(uuid.uuid4()),
                                     created_at=str(datetime.datetime.now()),
                                     **tmp_dict)
    return student_storage


def update_student_in_storage(id_old: uuid.UUID, student_new: StudentIn) -> StudentStorage:
    # Производит обновление данных студента

    tmp_dict: dict = student_new.dict()
    birth_date = str(tmp_dict.get('birth_date'))
    tmp_dict.update({'birth_date': birth_date})
    student_storage = StudentStorage(id=str(id_old),
                                     created_at=str(datetime.datetime.now()),
                                     **tmp_dict)

    return student_storage


def convert_student_dict_to_storage(student_dict: dict) -> StudentStorage:
    # Производит преобразование dict к типу StudentStorage

    student_storage = StudentStorage(**student_dict)
    return student_storage


