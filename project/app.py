from flask import Flask, render_template

from .users import users_bp
from .items import items_bp
from .db import init_app, db

app = Flask(__name__)
app.secret_key = 'TESTKEY'

# Register Blueprints
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(items_bp, url_prefix='/items')

# Root endpoint to render index.html
@app.route('/')
def index():
    return render_template('index.html')

with app.app_context():
    init_app(app)
    db.create_all()  # This will create all the tables defined in the app, including 'users'.

if __name__ == "__main__":
    app.run(debug=True)
