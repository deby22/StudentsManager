from flask import Blueprint
from flask.json import jsonify

from students_manager.models import User

users = Blueprint("users", __name__)


@users.route("/user", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([])


@users.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    product = User.query.get_or_404(id)
    return jsonify({})
