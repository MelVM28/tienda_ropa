from flask import Blueprint, jsonify, request
from ..models.venta import VentaModel

ventas_bp = Blueprint("ventas", __name__)

BASE = "/tienda/api/v1/ventas"

# ── GET todas las ventas ──────────────────────────────────────────────────────
@ventas_bp.route(BASE, methods=["GET"])
def get_all():
    return jsonify(VentaModel.get_all()), 200

# ── GET venta por ID ──────────────────────────────────────────────────────────
@ventas_bp.route(f"{BASE}/<id>", methods=["GET"])
def get_by_id(id):
    venta = VentaModel.get_by_id(id)
    if not venta:
        return jsonify({"error": "Venta no encontrada"}), 404
    return jsonify(venta), 200

# ── POST crear venta ──────────────────────────────────────────────────────────
@ventas_bp.route(BASE, methods=["POST"])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    nuevo_id = VentaModel.create(data)
    return jsonify({"mensaje": "Venta registrada", "id": nuevo_id}), 201

# ── PUT actualizar venta ──────────────────────────────────────────────────────
@ventas_bp.route(f"{BASE}/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    modificados = VentaModel.update(id, data)
    if modificados == 0:
        return jsonify({"error": "No se pudo actualizar"}), 404
    return jsonify({"mensaje": "Venta actualizada"}), 200

# ── DELETE eliminar venta ─────────────────────────────────────────────────────
@ventas_bp.route(f"{BASE}/<id>", methods=["DELETE"])
def delete(id):
    eliminados = VentaModel.delete(id)
    if eliminados == 0:
        return jsonify({"error": "No se pudo eliminar"}), 404
    return jsonify({"mensaje": "Venta eliminada"}), 200
