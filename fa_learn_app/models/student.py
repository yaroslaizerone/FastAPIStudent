import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseStudent(BaseModel):
    # Базовый класс для описания студента

    first_name: str
    last_name: str
    age: int
    birth_date: datetime.date
    login: str
    id_groupe: str


class StudentIn(BaseStudent):
    # Класс описывает студента, которого отправляет пользователь

    password: str


class StudentOut(BaseStudent):
    # Класс описывает студента, который отправляется пользователю (без секретной информации)

    id: uuid.UUID
    created_at: datetime.datetime


class StudentStorage(BaseStudent):
    # Класс описывает хранение студента в хранилище

    id: str
    birth_date: str
    created_at: str
    login: str
    password: str
