# reports/__init__.py
from flask import Blueprint

reports_bp = Blueprint('reports', __name__, url_prefix='/report')

from . import report  # Import report routes
