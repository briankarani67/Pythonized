from flask import Blueprint, jsonify
from models.user_model import get_all_users, add_user
from flask import request


user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods = ["GET"])
def users():
    data = get_all_users()
    return jsonify(data)

@user_bp.route("/users/post", methods=["POST"])
def create_user():

    data = request.json

    name = data["name"]
    email = data["email"]

    success = add_user(name, email)

    if success:
        return jsonify({
            "message": "User added successfully"
        })

    return jsonify({
        "error": "Failed to add user"
    })
