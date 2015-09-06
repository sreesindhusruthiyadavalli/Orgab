from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    
    user = {'name': 'Sruthi'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'name': 'Sruthi'}, 
            'body': 'Welcome to orgab!' 
        },
        { 
            'author': {'name': 'Sujay'}, 
            'body': "That's cool!"
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

    
