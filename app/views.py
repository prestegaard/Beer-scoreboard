from flask import render_template
from app import app
from .models import User


@app.route('/')
@app.route('/index')
def index():
    # user = User.query.get(3)
    users = User.query.all()
    criben = []
    criben.append(User.query.get(1)) # Vegard
    criben.append(User.query.get(7)) # Rune
    criben.append(User.query.get(3)) # Haagon
    criben.append(User.query.get(4)) # Simen
    criben.append(User.query.get(5)) # Vetle
    criben.append(User.query.get(2)) # Karlstad

    criben_old = []
    guests = []
    for u in users:
        if u.location == 'VIPs':
            criben_old.append(u)
        elif u.location == 'Guests':
            guests.append(u)

    # Format guests to be an n-by-6 matrix
    guests_formatted = [][]
    for row in xrange(0,len(guests)/6+1):
        for col in xrange(0,6):
             guests_formatted[row][col] = guests[row*6 + col]


    return render_template('user2.html',
                           criben_users=criben,
                           criben_users_old=criben_old,
                           guests_users=guests_formatted
                           )




