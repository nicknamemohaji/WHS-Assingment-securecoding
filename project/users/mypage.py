from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from ..db import get_db, User
from . import users_bp

##### CSRF Protection #####
from flask_wtf import FlaskForm
from wtforms import PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class MyPageForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired()])
    pw = PasswordField('Password')  # Use a password field for the password
    submit = SubmitField('Edit')
##### CSRF Protection #####


@users_bp.route('/mypage/<username>', methods=['GET'])
def mypage_get(username):
    db = get_db()
    user = db.query(User).filter_by(id=username).first()

    if not user:
        flash("User not found.", "error")
        return redirect(url_for('index'))

    is_self = session.get('user_id') == username
    form = MyPageForm(description=user.description)  # Initialize the form with existing data
    return render_template('users/mypage.html', user=user, is_self=is_self, form=form)

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

    form = MyPageForm()

    if form.validate_on_submit():  # Flask-WTF will automatically check CSRF and validate the form
        if form.description.data:
            user.description = form.description.data.strip()
        if form.pw.data:
            user.pw = form.pw.data.strip()

        db.commit()
        flash("Successfully updated.", "success")
        return redirect(url_for('users.mypage_get', username=username))

    flash("There were errors with your form submission.", "error")
    return render_template('users/mypage.html', user=user, is_self=True, form=form)
