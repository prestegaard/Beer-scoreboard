#!flask/bin/python
from app import db, models
import datetime

u = models.User.query.get(3)
u.last_seen = datetime.datetime.utcnow().strftime("%A, %d. %B %Y %H:%M")	
db.session.commit()

