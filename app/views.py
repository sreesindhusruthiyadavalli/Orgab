from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    
<<<<<<< HEAD
    #user = {'name': 'Sruthi'}  # fake user
    '''posts = [  # fake array of posts
=======
    user = {'name': 'Sruthi'}  
    posts = [  # array of posts
>>>>>>> 7cdb3074159a76a5a8ce8026f8ced77dd9693533
        { 
            'author': {'name': 'Sruthi'}, 
            'body': 'Welcome to orgab!' 
        },
        { 
            'author': {'name': 'Sujay'}, 
            'body': "That's cool!"
        }
    ]'''
    return render_template("orgab.html",
                           title='Home',
                           #user=user,
                           #posts=posts
                           )

    
