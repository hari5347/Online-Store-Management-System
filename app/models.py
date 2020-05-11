from app import db,login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32))
    name = db.Column(db.String(32))
    email = db.Column(db.String(32),index=True,unique=True)
    password = db.Column(db.String(128))
    def set_password(self,password):
        self.password = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password,password)

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    category = db.Column(db.String(32),index=True)
    price = db.Column(db.Float)
    description = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image = db.Column(db.String(128))
    quantity = db.Column(db.Integer)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))