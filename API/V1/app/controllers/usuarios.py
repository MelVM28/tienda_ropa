from flask import Blueprint, jsonify, request
from ..models.usuario import UsuarioModel

usuarios_bp = Blueprint("usuarios", __name__)

BASE = "/tienda/api/v1/usuarios"

# ── GET todos los usuarios ────────────────────────────────────────────────────
@usuarios_bp.route(BASE, methods=["GET"])
def get_all():
    return jsonify(UsuarioModel.get_all()), 200

# ── GET usuario por ID ────────────────────────────────────────────────────────
@usuarios_bp.route(f"{BASE}/<id>", methods=["GET"])
def get_by_id(id):
    usuario = UsuarioModel.get_by_id(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario), 200

# ── POST crear usuario ────────────────────────────────────────────────────────
@usuarios_bp.route(BASE, methods=["POST"])
def create():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    nuevo_id = UsuarioModel.create(data)
    return jsonify({"mensaje": "Usuario creado", "id": nuevo_id}), 201

# ── PUT actualizar usuario ────────────────────────────────────────────────────
@usuarios_bp.route(f"{BASE}/<id>", methods=["PUT"])
def update(id):
    data = request.get_json()
    modificados = UsuarioModel.update(id, data)
    if modificados == 0:
        return jsonify({"error": "No se pudo actualizar"}), 404
    return jsonify({"mensaje": "Usuario actualizado"}), 200

# ── DELETE eliminar usuario ───────────────────────────────────────────────────
@usuarios_bp.route(f"{BASE}/<id>", methods=["DELETE"])
def delete(id):
    eliminados = UsuarioModel.delete(id)
    if eliminados == 0:
        return jsonify({"error": "No se pudo eliminar"}), 404
    return jsonify({"mensaje": "Usuario eliminado"}), 200
