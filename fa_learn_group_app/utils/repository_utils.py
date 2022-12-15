import datetime
import uuid
from fa_learn_group_app.models.group import GroupIn, GroupStorage


def convert_group_in_to_storage(group: GroupIn) -> GroupStorage:
    # Производит конвертацию GroupIn --> GroupStorage

    tmp_dict: dict = group.dict()
    group_storage = GroupStorage(id=str(uuid.uuid4()),
                                 created_at=str(datetime.datetime.now()),
                                 **tmp_dict)
    return group_storage


def update_group_in_storage(id_old: uuid.UUID, group_new: GroupIn) -> GroupStorage:
    # Производит обновление данных группы

    tmp_dict: dict = group_new.dict()
    group_storage = GroupStorage(id=str(id_old),
                                 created_at=str(datetime.datetime.now()),
                                 **tmp_dict)

    return group_storage


def convert_group_dict_to_storage(group_dict: dict) -> GroupStorage:
    # Производит преобразование dict к типу GroupStorage

    group_storage = GroupStorage(**group_dict)
    return group_storage
