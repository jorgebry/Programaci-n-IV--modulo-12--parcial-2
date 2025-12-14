from flask import Blueprint, jsonify
import json

vacunas_bp = Blueprint("vacunas", __name__)

with open("data/vacunas_panama.json", encoding="utf-8") as f:
    datos = json.load(f)


@vacunas_bp.route("/vacunas", methods=["GET"])
def get_all():
    return jsonify({
        "pais": "Panamá",
        "indicador": "SH.IMM.MEAS",
        "datos": datos
    })


@vacunas_bp.route("/vacunas/<int:year>", methods=["GET"])
def get_by_year(year):
    for d in datos:
        if d["year"] == year:
            return jsonify(d)
    return jsonify({"error": "No hay datos para el año solicitado"}), 404


@vacunas_bp.route("/vacunas/provincia/<string:nombre>", methods=["GET"])
def get_by_provincia(nombre):
    ultimo = datos[-1]
    return jsonify({
        "provincia": nombre.lower(),
        "year": ultimo["year"],
        "coverage": ultimo["coverage"]
    })
