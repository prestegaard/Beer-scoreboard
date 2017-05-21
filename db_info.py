#!flask/bin/python
from app import db, models
import datetime
from datetime import *


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
