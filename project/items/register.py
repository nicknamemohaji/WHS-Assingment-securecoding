import os
import uuid

from flask import current_app, session
from werkzeug.utils import secure_filename
from . import items_bp
from ..db import get_db, Item
from flask import render_template, request, redirect, url_for, flash

##### CSRF Protection #####
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0, message="Price must be a positive number.")])
    image = FileField('Photo')
    submit = SubmitField('Register')
##### CSRF Protection #####

UPLOAD_FOLDER = 'static/uploads'

@items_bp.route('/register', methods=['GET'])
def register_get():
    form = ItemForm()  # Instantiate the form for GET request
    return render_template('items/register.html', form=form)

@items_bp.route('/register', methods=['POST'])
def register_post():
    form = ItemForm()  # Instantiate the form for POST request

    if form.validate_on_submit():  # Validate the form
        name = form.name.data
        description = form.description.data
        price = form.price.data
        file = form.image.data

        image_filename = None
        if file:
            os.makedirs(os.path.join(current_app.root_path, UPLOAD_FOLDER), exist_ok=True)
            image_filename = secure_filename(str(uuid.uuid4()))
            file.save(os.path.join(current_app.root_path, UPLOAD_FOLDER, image_filename))

        # Save the item in the database
        db = get_db()
        item = Item(name=name, description=description, image=image_filename, price=price, author=session.get('user_id'))
        db.add(item)
        db.commit()

        flash("Item registered successfully.", "success")
        return redirect(url_for('items.register_get'))

    # If form is invalid, re-render the form with errors
    flash("Please fill all fields correctly.", "error")
    return render_template('items/register.html', form=form)