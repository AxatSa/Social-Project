from fastapi import FastAPI

from photo.photoAPI import photo_router
from user.user_API import user_router
from post.user_post_api import posts_router
# для запуска БД
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(photo_router)
app.include_router(user_router)
app.include_router(posts_router)