from flask import Blueprint, jsonify, request
from ..models.marca import MarcaModel

marcas_bp = Blueprint("marcas", __name__)

BASE = "/tienda/api/v1/marcas"

# ── GET todas las marcas ──────────────────────────────────────────────────────
@marcas_bp.route(BASE, methods=["GET"])
def get_all():
    return jsonify(MarcaModel.get_all()), 200

# ── GET marca por ID ──────────────────────────────────────────────────────────
@marcas_bp.route(f"{BASE}/<id>", methods=["GET"])
def get_by_id(id):
    marca = MarcaModel.get_by_id(id)
    if not marca:
        return jsonify({"error": "Marca no encontrada"}), 404
    return jsonify(marca), 200

# ── POST crear marca ──────────────────────────────────────────────────────────
@marcas_bp.route(BASE, methods=["POST"])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    nuevo_id = MarcaModel.create(data)
    return jsonify({"mensaje": "Marca creada", "id": nuevo_id}), 201

# ── PUT actualizar marca ──────────────────────────────────────────────────────
@marcas_bp.route(f"{BASE}/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    modificados = MarcaModel.update(id, data)
    if modificados == 0:
        return jsonify({"error": "No se pudo actualizar"}), 404
    return jsonify({"mensaje": "Marca actualizada"}), 200

# ── DELETE eliminar marca ─────────────────────────────────────────────────────
@marcas_bp.route(f"{BASE}/<id>", methods=["DELETE"])
def delete(id):
    eliminados = MarcaModel.delete(id)
    if eliminados == 0:
        return jsonify({"error": "No se pudo eliminar"}), 404
    return jsonify({"mensaje": "Marca eliminada"}), 200
