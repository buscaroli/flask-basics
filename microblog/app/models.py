from datetime import datetime
from app import db, login
# werkzeug takes care of the hashing used in the password_hash field
# in the User class.
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Necessary for Flask-Login in order to be able to load a user
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# The class User inherits from the SQLAlchemy class db.Model
class User(UserMixin, db.Model):
    # Each field is created as an instance of the class db.Column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        '''Tells python how to print objects of this class, eg
        if given the username 'susan' it would print <User susan>'''
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    # The timestamp field is indexed so that we can retrieve
    # posts in chronological order
    # The user_is field is initialised as a foreign key to user.id
    # in order to reference an id value from the user table
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Post {}>'.format(self.body)
