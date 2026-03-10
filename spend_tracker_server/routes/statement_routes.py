import os
from flask import Blueprint, request, jsonify, current_app
from parsers.chase_parser import parse_chase_pdf

statement_bp = Blueprint("statements", __name__, url_prefix="/api/statements")


@statement_bp.route("", methods=["GET"])
def get_statements():
    return jsonify({
        "message": "Statement route working"
    }), 200


@statement_bp.route("/upload", methods=["POST"])
def upload_statement():

    data = request.get_json()

    filename = data.get("filename")
    bankname = data.get("bankname")

    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], bankname, filename)

    result = parse_chase_pdf(file_path)
    
    return jsonify(result), 200