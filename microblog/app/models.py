from app import db


## The class User inherits from the SQLAlchemy class db.Model
class User(db.Model):
    ## each field is created as an instance of the class db.Column
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        '''Tells python how to print objects of this class, eg
        if given the username 'susan' it would print <User susan>'''
        return '<User {}>'.format(self.username)