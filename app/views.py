from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid, socketio
from .models import User
import datetime







@app.route('/')
@app.route('/index')
def index():
   # user = User.query.get(3)
    users = User.query.all()

    return render_template('user2.html',
                           users=users
                           )




