from flask import Blueprint

bp = Blueprint('main', __name__)

from flask_application.app.main import routes
