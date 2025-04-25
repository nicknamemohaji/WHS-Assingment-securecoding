from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from ..db import get_db, User
from . import users_bp


@users_bp.route('/mypage/<username>', methods=['GET'])
def mypage_get(username):
    db = get_db()
    user = db.query(User).filter_by(id=username).first()

    if not user:
        flash("User not found.", "error")
        return redirect(url_for('index'))

    is_self = session.get('user_id') == username
    return render_template('users/mypage.html', user=user, is_self=is_self)

@users_bp.route('/mypage/<username>', methods=['POST'])
def mypage_post(username):
    if session.get('user_id') != username:
        flash("You can only edit your own profile.", "error")
        return redirect(url_for('users.mypage_get', username=username))

    db = get_db()
    user = db.query(User).filter_by(id=username).first()

    if not user:
        flash("User not found.", "error")
        return redirect(url_for('index'))

    if 'description' in request.form:
        user.description = request.form['description'].strip()
    if 'username' in request.form:
        user.pw = request.form['pw'].strip()

    db.commit()
    flash("Successfully updated.", "success")
    return redirect(url_for('users.mypage_get', username=username))
