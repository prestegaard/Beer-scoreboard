#!flask/bin/python
from app import db, models
import datetime
from datetime import *


beers = models.Beer.query.all()
users = models.User.query.all()


for u in users:
	for b in beers:
		if(b.drinker == u):
			print("User ID: {} Nickname: {}\t Beer number: {}\t Timestamp: {}\t".format(u.id, u.nickname, b.beer_number, b.timestamp).expandtabs(16))
