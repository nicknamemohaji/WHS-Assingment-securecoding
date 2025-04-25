from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from . import users_bp  # Importing the Blueprint from the users package
from ..db import get_db, User

@users_bp.route('/register', methods=['GET'])
def register_get():
    return render_template('users/register.html')

@users_bp.route('/register', methods=['POST'])
def register_post():
    user_id = request.form['username']
    password = request.form['password']

    # Check if user already exists
    existing_user = get_db().query(User).filter_by(id=user_id).first()
    if existing_user:
        flash("User already exists! Please choose a different username.", "error")
        return redirect(url_for('users.register'))

    # Create a new user instance
    new_user = User(id=user_id, pw=password)

    # Add the user to the database
    db = get_db()
    db.add(new_user)
    db.commit()

    # Auto-login after registration
    session['username'] = user_id  # Store the username in the session
    flash("Registration successful! You are now logged in.", "success")
    return redirect(url_for('index'))
