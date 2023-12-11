# app/auth/__init__.py

from flask import Blueprint

# Create a Blueprint instance for the auth package
auth = Blueprint('auth', __name__, template_folder='templates')

# Import the views and forms modules to associate them with the blueprint
# These imports are at the bottom to avoid circular dependencies, as these modules
# will need to import the 'auth' variable defined above
from . import views, forms