from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'matteo'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'What a Wonderful World'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'First commit..ehm comment!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)

@app.route('/index2')
def index2():
    user = {'username' : 'mark'}
    return render_template('index.html') 
    