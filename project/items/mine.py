from flask import render_template, session, redirect, url_for, flash, request, abort
from . import items_bp
from ..db import get_db, Item

@items_bp.route('/mine', methods=['GET'])
def mine_get():
    user_id = session.get('user_id')
    if not user_id:
        flash("로그인이 필요합니다.")
        return redirect(url_for('users.login_get'))

    db = get_db()
    items = db.query(Item).filter_by(author=user_id).order_by(Item.no.desc()).all()
    return render_template('items/mine.html', items=items)


@items_bp.route('/mine/<int:item_no>', methods=['POST'])
def mine_post(item_no):
    user_id = session.get('user_id')
    if not user_id:
        flash("로그인이 필요합니다.")
        return redirect(url_for('users.login_get'))

    db = get_db()
    item = db.query(Item).filter_by(no=item_no, author=user_id).first()

    if not item:
        abort(404)

    visibility = request.form.get('visible')
    if visibility == 'True':
        item.hide = False
        flash(f"Item {item.no}({item.name}) is visible")
    else:
        item.hide = True
        flash(f"Item {item.no}({item.name}) is hidden")

    db.commit()
    return redirect(url_for('items.mine_get'))
