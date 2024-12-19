from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Jovica"}

    posts = [
        {
            'author':{'username':'John'},
            'body': 'Nice day in Vancouver'
        },
        {
            'author':{'username':'Susan'},
            'body': 'The Wicked is a nice movie'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)



     