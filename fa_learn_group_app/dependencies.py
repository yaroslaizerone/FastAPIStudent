from fa_learn_app.repositories.student import StudentJsonRepository
from fa_learn_group_app.repositories.group import GroupJsonRepository



TMP_GROUP_REPOSITORY = GroupJsonRepository()




def get_group_repo() -> GroupJsonRepository:
    # Получение Group репозитория

    return TMP_GROUP_REPOSITORY
