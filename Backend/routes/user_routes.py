from flask import Blueprint, jsonify, request

from models.user_model import (
    get_all_users,
    add_user
)

from services.auth_service import hash_password


user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users", methods=["GET"])
def users():

    data = get_all_users()

    return jsonify(data)


@user_bp.route("/signup", methods=["POST"])
def signup():

    data = request.json

    name = data["name"]
    email = data["email"]
    password = data["password"]

    hashed_password = hash_password(password)

    success = add_user(
        name,
        email,
        hashed_password
    )

    if success:
        return jsonify({
            "message": "User created successfully"
        })

    return jsonify({
        "error": "Failed to create user"
    })