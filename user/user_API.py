from fastapi import APIRouter
from user import RegisterValidator, EditUserValidator

from database.userservice import register_user_db, get_all_users_db, delete_user_photo_db, add_profile_photo_db, get_exact_user_db

user_router = APIRouter(prefix='/user', tags=['Управление Пользователями'])

@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message':'Пользователь с такой почтой уже есть'}

@user_router.get('/get-user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users_db()

        return {'message': result}
    else:
        result = get_exact_user_db(user_id)

        return {'message': result}