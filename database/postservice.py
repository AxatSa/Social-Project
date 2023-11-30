from .models import UserPost, PostPhoto
from datetime import datetime

from database import get_db


# Добовление поста
def public_post_db(user_id, post_text):
    db = next(get_db())

    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=datetime.now())

    db.add(new_post)
    db.commit()
    return 'Успешно добалено'

def add_post_photo_db(post_id, post_photo):
    db = next(get_db())

    new_post_photo = PostPhoto(post_photo=post_photo, post_id=post_id)

    db.add(new_post_photo)
    db.commit()

    return 'Фото добвлено'

def change_post_db(post_id, user_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(id=post_id, user_id=user_id).first()

    if exact_post:
        exact_post.post_text = new_text

        db.commit()
        return 'Успешно измененно'
    else:
        return False

def delete_post_db(post_id):
    db = next(get_db())

    delete_post = db.query(UserPost).filter_by(id=post_id).first()
    delete_post_photo = db.query(PostPhoto).filter_by(post_id=post_id).first()

    if delete_post:
        # db.delete(delete_post_photo)
        # db.commit()

        db.delete(delete_post)
        db.commit()
        return 'Успешно удалено'
    else:
        return False

def get_exact_post_db(post_id):
    db  = next(get_db())
    exact_post = db.query(PostPhoto).filter_by(id=post_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Нету поста'

def get_all_posts_db():
    db = next(get_db())
    all_posts = db.query(UserPost).all()

    return all_posts

def get_exact_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(PostPhoto).filter_by(id=post_id).first()

    if exact_post:
        return exact_post
    else:
        return 'Error'