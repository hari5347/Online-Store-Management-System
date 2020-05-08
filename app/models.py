from app import db,login
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32))
    name = db.Column(db.String(32))
    email = db.Column(db.String(32),index=True,unique=True)
    password = db.Column(db.String(128))
    country = db.Column(db.String(16))
    address = db.Column(db.String(128))
    def set_password(self,password):
        self.password = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password,password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))