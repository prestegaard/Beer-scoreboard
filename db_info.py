#!flask/bin/python
from app import db, models
import datetime
from datetime import *
import math

beers = models.Beer.query.all()
users = models.User.query.all()

print ("############################")
print ("List of all beers per user")
for u in users:
	for b in beers:
		if b.user_id == u.id:
			print("Beer number : {}\t Drinker: {}\t Timestamp: {}\t".format(b.beer_number, u.nickname, b.timestamp).expandtabs(19))


print ("############################")
print ("List of all beers after time of drink")
user_nickname = ''
for b in beers:
    for u in users:
        if u.id == b.user_id:
            user_nickname = u.nickname
    print("Beer count  : {}\t Drinker: {}\t Timestamp: {}\t".format(b.id, user_nickname, b.timestamp).expandtabs(19))

print ("############################")
print ("Status overview of all users")
for u in users:
	number_of_beers = 0
	for b in beers:
		if b.user_id == u.id:
			number_of_beers += 1
	print("ID: {} {}\t {}\t Beers: {}\t {}\t".format(u.id, u.name, u.nickname, number_of_beers, u.button_color).expandtabs(13) + "{}\t {}\t".format(u.about_me, u.location).expandtabs(30))

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
guests_formatted = []
number_of_guest_rows = math.ceil(len(guests) / 6)
print("\n\n\n###### NUMBER OF ROWS FOR GUEST USERS: " + str(number_of_guest_rows))


# Creates a list containing number_of_guest_rows lists, each of number_of_guests items, all set to 0

Matrix = [[0 for x in range(0,6)] for y in range(number_of_guest_rows)]
#Matrix2 = [[6][number_of_guest_rows]]

for row in range(0, number_of_guest_rows):
    for col in range(0, 6):
        if  row * 6 + col < number_of_guests :
            Matrix[row][col] = guests[row * 6 + col]
            print("Row: " + str(row) + " Col: " + str(col) + " " + guests[row * 6 + col].nickname)
        else:
            break

line_number = 0
for row in Matrix:
    print("Guest line: " + str(line_number), end='')
    line_number += 1
    for user in row:
        print(", {}".format(user.nickname), end='')
    print("")