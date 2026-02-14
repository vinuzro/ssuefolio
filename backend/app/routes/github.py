from flask import Blueprint, jsonify

github_bp = Blueprint("github", __name__)

@github_bp.route("/health")
def health():
    return jsonify({"status": "ok"})
