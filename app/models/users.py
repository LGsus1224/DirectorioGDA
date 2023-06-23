from app.ext import db,login_manager
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __init__(self):
        super(Users,self).__init__()

    @classmethod
    def check_pass(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)