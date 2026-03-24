from .db import db
from bson import ObjectId

collection = db["prendas"]

class PrendaModel:

    @staticmethod
    def get_all():
        prendas = list(collection.find())
        for p in prendas:
            p["_id"] = str(p["_id"])
        return prendas

    @staticmethod
    def get_by_id(id):
        prenda = collection.find_one({"_id": ObjectId(id)})
        if prenda:
            prenda["_id"] = str(prenda["_id"])
        return prenda

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
