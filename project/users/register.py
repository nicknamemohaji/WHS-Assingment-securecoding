from flask import render_template, request, redirect, url_for, flash
from . import users_bp
from ..db import get_db, User

##### CSRF Protection #####
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=15)])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Register')
##### CSRF Protection #####


@users_bp.route('/register', methods=['GET'])
def register_get():
    form = RegisterForm()  # Create an empty form for the GET request
    return render_template('users/register.html', form=form)


@users_bp.route('/register', methods=['POST'])
def register_post():
    form = RegisterForm()

    if form.validate_on_submit():  # Checks if the form is valid and was submitted
        user_id = form.username.data
        password = form.password.data
        description = form.description.data

        db = get_db()

        if db.query(User).filter_by(id=user_id).first():
            flash("User ID already exists.", "error")
            return redirect(url_for('users.register_get'))

        new_user = User(id=user_id, pw=password, description=description)
        db.add(new_user)
        db.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('users.login_get'))

    # If form validation fails, re-render the form with error messages
    return render_template('users/register.html', form=form)