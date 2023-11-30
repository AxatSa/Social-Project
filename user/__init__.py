from pydantic import BaseModel


# Валидатор для входа в аккаунт
class LoginUserValidator(BaseModel):
    email: str
    password: str


# Валидатор для регистрации
class RegisterValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    city: str
    password: str


# Валидатор для изменения пользователя
class EditUserValidator(BaseModel):
    user_id: int
    surname: str
    new_data: str
