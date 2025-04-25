from flask import Blueprint

users_bp = Blueprint('users', __name__)

# Importing routes after blueprint definition
from . import register, login
