from flask import render_template, redirect, url_for, request, flash
from . import admin_bp
from ..db import db, Item

@admin_bp.route('/items/list')
def admin_items_list():
    items = Item.query.all()
    return render_template('admin/items_list.html', items=items)

@admin_bp.route('/items/<int:id>', methods=['POST'])
def admin_item_toggle_visibility(id):
    item = Item.query.get_or_404(id)
    visibility = request.form.get('visible')

    if visibility == 'False':
        item.hide = True
        flash(f"Item {item.no} ({item.name}) is now hidden.", "success")
    else:
        item.hide = False
        flash(f"Item {item.no} ({item.name}) is now visible.", "success")

    db.session.commit()
    return redirect(url_for('admin.admin_items_list'))
