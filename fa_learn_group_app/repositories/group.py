from typing import List, Dict, Optional
import uuid
from fa_learn_group_app.models.group import GroupIn, GroupStorage
from fa_learn_group_app.utils.json_repository import data_groups, save_dict_to_json
from fa_learn_group_app.utils.repository_utils import convert_group_in_to_storage, update_group_in_storage, convert_group_dict_to_storage


class BaseGroupRepository:
    # Базовый класс для реализации функционала работы с группами

    def get_by_id(self, id: uuid.UUID) -> GroupStorage:
        raise NotImplementedError

    def get_all(self, limit: int, skip: int) -> List[GroupStorage]:
        raise NotImplementedError

    def create(self, group: GroupIn) -> GroupStorage:
        raise NotImplementedError

    def update_by_id(self, id: uuid.UUID, group: GroupIn) -> GroupStorage:
        raise NotImplementedError

    def delete_by_id(self, id: uuid.UUID) -> GroupStorage:
        raise NotImplementedError


class GroupJsonRepository(BaseGroupRepository):
    # Реализация группы с хранилищем json

    def get_by_id(self, id: uuid.UUID) -> Optional[GroupStorage]:
        # Получение группы по id

        group: GroupStorage = data_groups.get(str(id))
        if group is None:
            return "Группа не найдена"
        group_out = convert_group_dict_to_storage(group)
        return group_out

    def get_all(self, limit: int, skip: int) -> List[GroupStorage]:
        # Получение всех групп

        group_out_list: List[GroupStorage] = []
        for _, group in data_groups.items():
            if group == "":
                group_out_list.append(convert_group_dict_to_storage(group))
            elif group.get("group") == group:
                group_out_list.append(convert_group_dict_to_storage(group))
        return group_out_list[skip:skip + limit]

    def create(self, group: GroupIn) -> GroupStorage:
        # Создание группы

        group_storage: GroupStorage = convert_group_in_to_storage(group)
        data_groups.update({str(group_storage.id): group_storage.dict()})
        save_dict_to_json()
        return group_storage

    def update_by_id(self, id: uuid.UUID, group_new: GroupIn) -> Optional[GroupStorage]:
        # Получение группы по id для обновления данных

        group_old: GroupStorage = data_groups.get(str(id))
        if group_old is None:
            return "Группа не найдена"

        group_update: GroupStorage = update_group_in_storage(id, group_new)
        data_groups.update({str(group_update.id): group_update.dict()})
        save_dict_to_json()
        return group_update

    def delete_by_id(self, id: uuid.UUID) -> str:
        # Удаление группы по id

        group: GroupStorage = data_groups.get(str(id))
        if group is None:
            return "Группа не найдена"
        data_groups.pop(str(id), None)
        save_dict_to_json()
        return "Группа успешно удалена"
