from flask import render_template, abort
from . import items_bp
from ..db import get_db, Item

@items_bp.route('/<int:item_no>', methods=['GET'])
def inspect_get(item_no):
    db = get_db()
    item = db.query(Item).filter_by(no=item_no, hide=False).first()

    if not item:
        abort(404)

    return render_template('items/details.html', item=item)

