from bson import ObjectId as objectid
from fastapi import APIRouter, HTTPException

from models.user import User
from config.db import conn
from schemas.user import userEntiry, usersEntity


user = APIRouter()


@user.get('/')
async def get_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find())


@user.get('/{id}')
async def get_one_user(id):
    return userEntiry(conn.local.user.find_one({"_id": objectid(id)}))

@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())



@user.put('/{id}')
async def update_user(id, user: User):
    conn.local.user.find_one_and_update({"_id": objectid(id)}, {"$set": (dict(user))})
    return userEntiry(conn.local.user.find_one({"_id": objectid(id)}))

@user.delete('/{id}')
async def delete_user(id):
    user = conn.local.user.find_one_and_delete({"_id": objectid(id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"deleted": "Succesfully deleted"}
