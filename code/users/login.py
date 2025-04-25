# users/login.py
from flask import render_template, request, redirect, url_for, flash, session
from . import users_bp  # Importing the Blueprint from the users package
from db import get_db, User

@users_bp.route('/login', methods=['GET'])
def login_get():
    return render_template('users/login.html')

@users_bp.route('/login', methods=['POST'])
def login_post():
    user_id = request.form['username']
    password = request.form['password']

    # Query the user from the database
    user = get_db().query(User).filter_by(id=user_id).first()

    if user and user.pw == password:
        # Authentication successful
        session['user_id'] = user_id
        flash("Login successful! Welcome back.", "success")
        return redirect(url_for('index'))  # Redirect to the homepage or dashboard
    else:
        flash("Invalid username or password. Please try again.", "error")
        return redirect(url_for('users.login_get'))
