from app import app, db
from app.models import User, Post

## We are adding some context to the flask shell so that
## if we run flask shell, we can start hacking around with
## all the required variables in memory
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


