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

    maggas_place = []
    guests = []
    for u in users:
        if u.location == 'Maggas place':
            maggas_place.append(u)
        elif u.location == 'Guest':
            guests.append(u)

    return render_template('user2.html',
                           criben_users=criben,
                           magga_users=maggas_place,
                           guests_users=guests
                           )




