from flask import Blueprint

frente = Blueprint('frente', __name__, template_folder='templates', static_folder='static')
from . import frent
