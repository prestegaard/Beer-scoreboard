from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .models import User
import datetime



@app.route('/')
@app.route('/index')
def index():
    user = "Haagon"
    beer = [  # fake array of posts
        { 
            'Drinker': {'nickname': 'Haagon'}, 
            'When':  datetime.datetime.utcnow().strftime("%A, %d. %B %Y %H:%M")

        },
        { 
            'Drinker': {'nickname': 'Susan'}, 
            'When': datetime.datetime.utcnow().strftime("%A, %d. %B %Y %H:%M")

        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           beer=beer)


@app.route('/toilet')
def toilet():
    return render_template("toilet.html")



@app.route('/users')
def users():
   # user = User.query.get(3)
    users = User.query.all()

#    posts = [
#        {'author': user, 'body': 'Test post #1'},
#        {'author': user, 'body': 'Test post #2'}
#    ]
    return render_template('user.html',
                           users=users
    #                       user=user,
    #                       posts=posts
                           )
