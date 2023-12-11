# app/main/views.py
from flask import render_template, request, current_app, redirect, url_for
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
def about():
    return render_template('about.html')

# Add more routes for your main application features below
