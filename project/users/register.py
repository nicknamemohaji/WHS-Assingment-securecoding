from flask import render_template, request, redirect, url_for, flash
from . import users_bp
from ..db import get_db, User

@users_bp.route('/register', methods=['GET'])
def register_get():
    return render_template('users/register.html')

@users_bp.route('/register', methods=['POST'])
def register_post():
    user_id = request.form['username']
    password = request.form['password']
    description = request.form.get('description', '')

    db = get_db()

    if db.query(User).filter_by(id=user_id).first():
        flash("User ID already exists.", "error")
        return redirect(url_for('users.register_get'))

    new_user = User(id=user_id, pw=password, description=description)
    db.add(new_user)
    db.commit()

    flash("Registration successful! Please log in.", "success")
    return redirect(url_for('users.login_get'))
