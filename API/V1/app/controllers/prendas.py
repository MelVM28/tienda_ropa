from flask import Blueprint, jsonify, request
from ..models.prenda import PrendaModel

prendas_bp = Blueprint("prendas", __name__)

BASE = "/tienda/api/v1/prendas"

# ── GET todas las prendas ─────────────────────────────────────────────────────
@prendas_bp.route(BASE, methods=["GET"])
def get_all():
    return jsonify(PrendaModel.get_all()), 200

# ── GET prenda por ID ─────────────────────────────────────────────────────────
@prendas_bp.route(f"{BASE}/<id>", methods=["GET"])
def get_by_id(id):
    prenda = PrendaModel.get_by_id(id)
    if not prenda:
        return jsonify({"error": "Prenda no encontrada"}), 404
    return jsonify(prenda), 200

# ── POST crear prenda ─────────────────────────────────────────────────────────
@prendas_bp.route(BASE, methods=["POST"])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    nuevo_id = PrendaModel.create(data)
    return jsonify({"mensaje": "Prenda creada", "id": nuevo_id}), 201

# ── PUT actualizar prenda ─────────────────────────────────────────────────────
@prendas_bp.route(f"{BASE}/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    modificados = PrendaModel.update(id, data)
    if modificados == 0:
        return jsonify({"error": "No se pudo actualizar"}), 404
    return jsonify({"mensaje": "Prenda actualizada"}), 200

# ── DELETE eliminar prenda ────────────────────────────────────────────────────
@prendas_bp.route(f"{BASE}/<id>", methods=["DELETE"])
def delete(id):
    eliminados = PrendaModel.delete(id)
    if eliminados == 0:
        return jsonify({"error": "No se pudo eliminar"}), 404
    return jsonify({"mensaje": "Prenda eliminada"}), 200
