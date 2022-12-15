from fa_learn_app.repositories.student import StudentJsonRepository
from fa_learn_group_app.repositories.group import GroupJsonRepository


TMP_STUDENT_REPOSITORY = StudentJsonRepository()



def get_student_repo() -> StudentJsonRepository:
    # Получение Student репозитория

    return TMP_STUDENT_REPOSITORY



