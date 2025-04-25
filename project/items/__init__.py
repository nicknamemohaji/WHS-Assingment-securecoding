from flask import Blueprint

items_bp = Blueprint('items', __name__)

# Importing routes after blueprint definition
from . import register, recent
