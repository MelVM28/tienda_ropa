from .db import db
from bson import ObjectId

collection    = db["ventas"]
col_prendas   = db["prendas"]

class VentaModel:

    @staticmethod
    def get_all():
        ventas = list(collection.find())
        for v in ventas:
            v["_id"] = str(v["_id"])
        return ventas

    @staticmethod
    def get_by_id(id):
        venta = collection.find_one({"_id": ObjectId(id)})
        if venta:
            venta["_id"] = str(venta["_id"])
        return venta

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

    # ── Reporte: marcas que tienen al menos una venta ──────────────────────────
    @staticmethod
    def marcas_con_ventas():
        pipeline = [
            { "$unwind": "$prendas" },
            {
                "$lookup": {
                    "from": "prendas",
                    "localField": "prendas.nombre",
                    "foreignField": "nombre",
                    "as": "detalle_prenda"
                }
            },
            { "$unwind": "$detalle_prenda" },
            {
                "$group": {
                    "_id": "$detalle_prenda.marca",
                    "totalVentas":   { "$sum": 1 },
                    "totalPrendas":  { "$sum": "$prendas.cantidad" }
                }
            },
            { "$sort": { "totalVentas": -1 } }
        ]
        result = list(collection.aggregate(pipeline))
        return result
