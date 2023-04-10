from flask_login import UserMixin
from datetime import datetime
from .extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True, 
                         index=True)
    password = db.Column(db.Text)
    email = db.Column(db.String(50), unique=True,
                      index=True)
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, default=datetime.now())