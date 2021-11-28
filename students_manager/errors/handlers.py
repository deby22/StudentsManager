from flask import Blueprint
from flask.json import jsonify

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(404)
def error_404(error):
    return jsonify({}), 404
