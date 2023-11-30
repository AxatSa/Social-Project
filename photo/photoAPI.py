from fastapi import APIRouter, UploadFile

photo_router = APIRouter(prefix='/photo', tags=['Фотографии'])

# Добавление фото
@photo_router.post('/add-photo')
async def add_user_photo(photo_file: UploadFile, user_id: int):
    # сохранить локально фото
    print(photo_file.filename)
    print(photo_file.file)
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)
    return {'status': 1, 'message': 'chiki piki'}


# Изменение фото
@photo_router.put('/edit-photo')
async def edit_user_profile_photo(user_id: int, new_photo: UploadFile):
    print(new_photo.filename)
    print(new_photo.file)
    with open(f'media/{new_photo.filename}', 'wb') as file:
        user_photo = await new_photo.read()

        file.write(user_photo)
    return {'status': 2, 'message': 'photo izmemeneno chiki piki'}


# Удаление фото
@photo_router.delete('/delete_photo')
async def delete_photo(user_id: int, photo_id: int):
    pass
