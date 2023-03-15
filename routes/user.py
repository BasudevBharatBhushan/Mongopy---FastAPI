from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import serializeDict, serializeList
from bson.objectid import ObjectId as objectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(serializeList(conn.local.user.find()))
    return serializeList(conn.local.user.find())

@user.get('/{id}')
async def find_user(id):
    return serializeDict(conn.local.user.find_one({"_id":objectId(id)}))


@user.post('/')
async def create_user(user: User):
    result = conn.local.user.insert_one(dict(user))
    inserted_id = result.inserted_id
    inserted_user = conn.local.user.find_one({"_id": inserted_id})
    return serializeDict(inserted_user)


@user.put('/{id}')
async def update_user(id, user:User):
    conn.local.user.find_one_and_update({"_id":objectId(id)}, {"$set":dict(user)})
    return serializeDict(conn.local.user.find_one({"_id":objectId(id)}))


@user.delete('/{id}')
async def delete_user(id):
    conn.local.user.find_one_and_delete({"_id":objectId(id)})
    return {"message":"User deleted successfully"}
   