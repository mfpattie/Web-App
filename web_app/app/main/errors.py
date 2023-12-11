# app/main/errors.py
from flask import render_template
from . import main


@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@main.errorhandler(500)
def internal_error(error):
    # insert any error logging or handling mechanism here
    return render_template('500.html'), 500

# You can add custom error handlers for other error codes if needed
