from flask import Blueprint, jsonify
from models.user_model import get_all_users

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods = ["GET"])
def users():
    data = get_all_users()
    return jsonify(data)