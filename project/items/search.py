from flask import request, render_template
from . import items_bp
from ..db import get_db, Item

@items_bp.route('/search', methods=['GET'])
def item_search_get():
    query = request.args.get('query', '').strip()
    order = request.args.get('order', 'asc')
    db = get_db()

    if query:
        q = db.query(Item).filter(Item.name.ilike(f"%{query}%"), Item.hide == False)
        if order == 'desc':
            q = q.order_by(Item.price.desc())
        else:
            q = q.order_by(Item.price.asc())
        results = q.all()
    else:
        results = []

    return render_template('items/search.html', items=results, query=query)
