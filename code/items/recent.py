from flask import jsonify
from . import items_bp
from db import get_db, Item

@items_bp.route('/recents', methods=['GET'])
def recents():
    """Handles the GET request for returning recent items as JSON."""
    # Fetch recent items from the database or a static list
    recent_items: list[Item]
    recent_items = get_db().query(Item).order_by(Item.no.desc()).limit(5).all()

    return jsonify([
        {'name': item.name, 'price': item.price} for item in recent_items
    ])  # Return the list as a JSON response
