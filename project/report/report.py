from flask import render_template, request, redirect, url_for, flash, session
from . import reports_bp
from ..db import get_db, Report, User

##### CSRF Protection #####
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ReportForm(FlaskForm):
    target = StringField('Target Username', validators=[DataRequired()])
    reason = TextAreaField('Reason', validators=[DataRequired()])
    submit = SubmitField('Submit Report')
##### CSRF Protection #####


@reports_bp.route('/report', methods=['GET'])
def report_get():
    form = ReportForm()  # Create an empty form for GET request
    return render_template('reports/report.html', form=form)

@reports_bp.route('/report', methods=['POST'])
def report_post():
    user_id = session.get('user_id')
    if not user_id:
        flash("You need to be logged in to report.", "error")
        return redirect(url_for('users.login_get'))

    form = ReportForm()  # Instantiate the form on POST request
    if form.validate_on_submit():  # This validates the form and checks CSRF token
        target_username = form.target.data
        reason = form.reason.data

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

    # If form is invalid, re-render the form with errors
    flash("There were errors with your submission.", "error")
    return render_template('reports/report.html', form=form)
