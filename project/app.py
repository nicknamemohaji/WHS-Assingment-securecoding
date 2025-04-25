from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.csrf import CSRFProtect


from .users import users_bp
from .items import items_bp
from .report import reports_bp
from .admin import admin_bp
from .db import init_app, db

app = Flask(__name__)
app.secret_key = 'TESTKEY'

# Root endpoint to render index.html
@app.route('/')
def index():
    return render_template('index.html')

@admin_bp.route('/')
def admin_index_get():
    return render_template('admin/admin_index.html')


# Register Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(items_bp, url_prefix='/items')
app.register_blueprint(reports_bp, url_prefix='/report')
app.register_blueprint(admin_bp, url_prefix='/admin')


with app.app_context():
    init_app(app)
    db.create_all()  # This will create all the tables defined in the app, including 'users'.

if __name__ == "__main__":
    app.run(debug=True)
