import os
import uuid

from flask import current_app, session
from werkzeug.utils import secure_filename
from . import items_bp
from ..db import get_db, Item
from flask import render_template, request, redirect, url_for, flash

UPLOAD_FOLDER = 'static/uploads'

@items_bp.route('/register', methods=['GET'])
def register_get():
    return render_template('items/register.html')

@items_bp.route('/register', methods=['POST'])
def register_post():
    try:
        name = request.form['name']
        description = request.form['description']
        file = request.files['image']
        price = int(request.form['price'])
    except KeyError:
        flash('Please fill all fields', 'error')
        return redirect(url_for('register_get'))
    image_filename = None
    if file and file.filename:
        os.makedirs(os.path.join(current_app.root_path, UPLOAD_FOLDER), exist_ok=True)
        image_filename = secure_filename(str(uuid.uuid4()))
        file.save(os.path.join(current_app.root_path, UPLOAD_FOLDER, image_filename))
    else:
        flash('No file', 'error')
        return redirect(url_for('register_get'))

    db = get_db()
    item = Item(name=name, description=description, image=image_filename, price=price, author=session.get('user_id'))
    db.add(item)
    db.commit()

    flash("Item registered successfully.", "success")
    return redirect(url_for('items.register_get'))
