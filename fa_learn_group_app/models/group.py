from pydantic import BaseModel


class GroupIn(BaseModel):
    # Базовый класс для описания группы

    name: str


class GroupStorage(GroupIn):
    # Класс описывает хранение группы в хранилище

    id: str
    created_at: str
