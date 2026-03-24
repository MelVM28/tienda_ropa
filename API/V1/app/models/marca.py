from .db import db
from bson import ObjectId

collection = db["marcas"]

class MarcaModel:

    @staticmethod
    def get_all():
        marcas = list(collection.find())
        for m in marcas:
            m["_id"] = str(m["_id"])
        return marcas

    @staticmethod
    def get_by_id(id):
        marca = collection.find_one({"_id": ObjectId(id)})
        if marca:
            marca["_id"] = str(marca["_id"])
        return marca

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
