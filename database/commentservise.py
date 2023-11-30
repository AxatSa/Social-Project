from .models import Coment

from datetime import datetime

from database import get_db


def add_comment_db(comment_text, user_id, post_id):
    db = next(get_db())
    new_comment = Coment(user_id=user_id,
                         comment_text=comment_text,
                         post_id=post_id)

    db.add(new_comment)
    db.commit()
    return 'Коментарий Успешно добалено'


def edit_comment_db(comment_id, new_comment):
    db = next(get_db())

    edit_comment = db.query(Coment).filter_by(id=post_id, user_id=user_id, comment_text=comment_text).firedit
    if edit_comment:
        edit_comment.comment_text = new_comment

        db.commit()
        return 'Rjvtynhfq успешно измененно'
    else:
        return False


def delete_comment_db(comment_id):
    db = next(get_db())

    delete_comment = db.query(Coment).felter_by(comment_id=comment_id).first()

    if delete_post:
        db.delete(delete_comment)
        db.commit()

        return 'Успешно удалено'
    else:
        return False


def get_post_comment(post_id):
    db = next(get_db())

    post_comment = db.query(Coment).filter_by(post_id=post_id).first()
    return post_comment
