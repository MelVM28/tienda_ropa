from .db import db
from bson import ObjectId

collection = db["usuarios"]

class UsuarioModel:

    @staticmethod
    def get_all():
        usuarios = list(collection.find())
        for u in usuarios:
            u["_id"] = str(u["_id"])
        return usuarios

    @staticmethod
    def get_by_id(id):
        usuario = collection.find_one({"_id": ObjectId(id)})
        if usuario:
            usuario["_id"] = str(usuario["_id"])
        return usuario

    @staticmethod
    def create(data):
        result = collection.insert_one(data)
        return str(result.inserted_id)

    @staticmethod
    def update(id, data):
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return result.modified_count

    @staticmethod
    def delete(id):
        result = collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count
