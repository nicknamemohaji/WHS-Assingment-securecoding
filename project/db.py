from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # SQLite database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(15), primary_key=True)
    pw = db.Column(db.String(20))

class Item(db.Model):
    __tablename__ = 'items'
    no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

def get_db():
    return db.session
