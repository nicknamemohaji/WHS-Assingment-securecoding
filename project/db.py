from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # SQLite database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(15), primary_key=True)  # Login ID
    pw = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text)

    admin = db.Column(db.Boolean, default=False)  # New column for admin role
    banned = db.Column(db.Boolean, default=False)  # New column for banned status

class Item(db.Model):
    no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    hide = db.Column(db.Boolean, default=False)
    image = db.Column(db.Text)  # Store image filename or path
    author = db.Column(db.String(15), db.ForeignKey('users.id'), nullable=False)

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reporter = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    target = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    resolved = db.Column(db.Boolean, default=False)

    reporter_user = db.relationship('User', foreign_keys=[reporter])
    target_user = db.relationship('User', foreign_keys=[target])

def get_db():
    return db.session
