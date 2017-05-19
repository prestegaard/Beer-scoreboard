from flask import render_template
from app import app
from .models import User


@app.route('/')
@app.route('/index')
def index():
   # user = User.query.get(3)
    #users = User.query.all()
    users = []
    users.append(User.query.get(1)) # Vegard
    users.append(User.query.get(7)) # Rune
    users.append(User.query.get(3)) # Haagon
    users.append(User.query.get(4)) # Simen
    users.append(User.query.get(5)) # Vetle
    users.append(User.query.get(2)) # Karlstad

    return render_template('user2.html',
                           users=users
                           )




