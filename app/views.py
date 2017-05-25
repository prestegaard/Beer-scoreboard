from flask import render_template
from app import app
from .models import User
import math


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
    number_of_guests = 0
    for u in users:
        if u.location == 'VIPs':
            criben_old.append(u)
        elif u.location == 'Guests':
            number_of_guests += 1
            guests.append(u)

    # Format guests to be an n-by-6 matrix
    number_of_guest_rows = math.ceil(len(guests) / 6)
    print("\n\n\n###### NUMBER OF ROWS FOR GUEST USERS: " + str(number_of_guest_rows))

    # Creates a list containing number_of_guest_rows lists
    Matrix = [[] for x in range(0, number_of_guest_rows)]

    for row in range(0, number_of_guest_rows):
        for col in range(0, 6):
            if row * 6 + col < number_of_guests:
                Matrix[row].append(guests[row * 6 + col])
                print("Row: " + str(row) + " Col: " + str(col) + " " + guests[row * 6 + col].nickname)
            else:
                break

    line_number = 0
    for row in Matrix:
        print("Guest line: " + str(line_number), end='')
        line_number += 1
        for user in row:
            if not user == 0 :
                print(", {}".format(user.nickname), end='')
        print("")

    return render_template('user2.html',
                           criben_users=criben,
                           criben_old=criben_old,
                           guests_users=Matrix
                           )





