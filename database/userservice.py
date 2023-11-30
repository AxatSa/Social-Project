from database.models import User

from database import get_db

from datetime import datetime


# Rегистрация пользователя
def register_user_db(name, surname, email,
                     phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return "Успешно"

    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number,
                    city=city, password=password, reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return 'Успешно прошли регистрацию'

def add_profile_photo_db(profile_photo, user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(id=user_id).first()

    if checker:
        checker.profile_photo = profile_photo
        db.commit()
        return 'фото профиля добавлен'
    else:
        return False

# изменение данных
def delete_user_photo_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(id=user_if).first()

    if checker:
        checker.profile_photo = 'None'
        db.commit()

        return 'Фото профиля удалено'

    else:
        return False

# олучить bbox пользователей
def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users

def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(id=user_id).first()

    return exact_user
