from flask import render_template, redirect, url_for, request, flash
from . import admin_bp
from ..db import db, Report, User, Item

##### CSRF Protection #####
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

# Form for acting on reports (e.g., ban user, hide item)
class ReportActionForm(FlaskForm):
    action = SelectField('Action', choices=[('ban_user', 'Ban User'), ('hide_item', 'Hide Item')], coerce=str)
    submit = SubmitField('Submit Action')
##### CSRF Protection #####


@admin_bp.route('/reports/')
def admin_reports():
    reports = Report.query.filter_by(resolved=False).all()
    return render_template('admin/reports_list.html', reports=reports)

@admin_bp.route('/reports/<int:id>')
def admin_report_view(id):
    report = Report.query.get_or_404(id)
    form = ReportActionForm()  # Initialize the form for action on the report
    return render_template('admin/report_view.html', report=report, form=form)

@admin_bp.route('/reports/<int:id>/act', methods=['POST'])
def admin_report_act(id):
    report = Report.query.get_or_404(id)
    form = ReportActionForm()  # Initialize form to access CSRF token

    if form.validate_on_submit():  # Ensure CSRF validation
        action = form.action.data  # Retrieve the selected action from the form

        if action == 'ban_user':
            target_user = User.query.get(report.target)
            target_user.banned = True
            flash("User has been banned.", "success")
        elif action == 'hide_item':
            target_item = Item.query.get(report.target)
            target_item.hide = True
            flash("Item has been hidden.", "success")

        report.resolved = True
        db.session.commit()

        return redirect(url_for('admin.admin_reports'))

    flash('Invalid form submission.', 'error')
    return redirect(url_for('admin.admin_report_view', id=id))

@admin_bp.route('/reports/resolved')
def admin_reports_resolved():
    reports = Report.query.filter_by(resolved=True).all()
    return render_template('admin/reports_list_resolved.html', reports=reports)
