from fastapi import APIRouter

from comments import CommentValidator, EditCommentValidator

from database import add_comment_db, edit_comment_db, delete_post_db, get_post_comments_db

comment_router = APIRouter(prefix='/comment', tags=['Работа с коментариями'])

@comment_router.post('/add_comment')
async def add_comment(data: CommentValidator):
    pass

@comment_router.put('/edit_comment')
async def edit_comment(data:EditCommentValidator):
    pass

@comment_router.delete('/delete_comment')
async def delete_comment(comment_id: int):
    pass

@comment_router.get('/get_comments')
async def get_comments(post_id: int):
    pass

