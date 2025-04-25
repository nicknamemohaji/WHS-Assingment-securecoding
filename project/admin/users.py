from flask import render_template, redirect, url_for, request, flash
from . import admin_bp
from ..db import db, User

@admin_bp.route('/users/list')
def admin_users_list():
    users = User.query.all()
    return render_template('admin/users_list.html', users=users)

@admin_bp.route('/users/<string:id>', methods=['POST'])
def admin_user_toggle_ban(id):
    user = User.query.get_or_404(id)
    action = request.form.get('action')

    if action == 'ban':
        user.banned = True
        flash(f"User {user.id} has been banned.", "success")
    elif action == 'unban':
        user.banned = False
        flash(f"User {user.id} has been unbanned.", "success")

    db.session.commit()
    return redirect(url_for('admin.admin_users_list'))
