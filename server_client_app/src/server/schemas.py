from pydantic import BaseModel, validator

MIN_PASSWORD_LENGTH = 8


class UserCreate(BaseModel):
    login: str
    password: str

    @validator('password')
    def min_length(cls, value):
        if len(value) < MIN_PASSWORD_LENGTH:
            raise ValueError(f'Длина пароля не может быть меньше {MIN_PASSWORD_LENGTH} символов.')
        return value


class User(BaseModel):
    id: int
    login: str

    class Config:
        orm_mode = True
