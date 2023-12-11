# app/main/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__)

# This import statement is placed at the end to avoid circular dependencies.
from . import views, errors
