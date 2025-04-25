from flask import render_template, request, redirect, url_for, flash, session
from . import reports_bp
from ..db import get_db, Report, User

@reports_bp.route('/report', methods=['GET'])
def report_get():
    return render_template('reports/report.html')

@reports_bp.route('/report', methods=['POST'])
def report_post():
    user_id = session.get('user_id')
    if not user_id:
        flash("You need to be logged in to report.", "error")
        return redirect(url_for('users.login_get'))

    target_username = request.form.get('target')
    reason = request.form.get('reason')

    if not target_username or not reason:
        flash("Target and reason are required.", "error")
        return redirect(url_for('reports.report_get'))

    db = get_db()
    target_user = db.query(User).filter_by(id=target_username).first()

    if not target_user:
        flash("Target user not found.", "error")
        return redirect(url_for('reports.report_get'))

    # Create new report
    new_report = Report(reporter=user_id, target=target_user.id, reason=reason)
    db.add(new_report)
    db.commit()

    flash("Report has been successfully submitted.", "success")
    return redirect(url_for('reports.report_get'))
