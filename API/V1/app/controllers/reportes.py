from flask import Blueprint, jsonify
from ..models.venta import VentaModel

reportes_bp = Blueprint("reportes", __name__)

BASE = "/tienda/api/v1/reportes"

# ── Reporte: marcas que tienen al menos una venta ─────────────────────────────
@reportes_bp.route(f"{BASE}/marcas-con-ventas", methods=["GET"])
def marcas_con_ventas():
    resultado = VentaModel.marcas_con_ventas()
    return jsonify(resultado), 200
