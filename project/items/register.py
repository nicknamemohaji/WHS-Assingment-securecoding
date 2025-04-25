from flask import render_template, request, redirect, url_for, flash
from . import items_bp
from ..db import get_db, Item

@items_bp.route('/register', methods=['GET'])
def register_get():
    return render_template('items/register.html')

@items_bp.route('/register', methods=['POST'])
def register_post():
    item_name = request.form['name']
    item_price = request.form['price']

    # Create a new item instance
    new_item = Item(name=item_name, price=int(item_price))

    # Add the item to the database
    db = get_db()
    db.add(new_item)
    db.commit()

    flash("Item added successfully!", "success")
    return redirect(url_for('index'))
