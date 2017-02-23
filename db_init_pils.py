#!flask/bin/python
from app import db, models
import datetime
users = models.User.query.all()

for u in users:
	db.session.delete(u)
db.session.commit()

u = models.User(name='Vegard', nickname='Laowi', 	number_of_beers=1, 	 about_me='Eg e ein Revolveman.', 		button_color='blue', 	img_src='/static/images/vegard.jpg')
db.session.add(u)
u = models.User(name='Øyvind', nickname='Karlstad', number_of_beers=14,  about_me='Je et flesk og pannkak.', 	button_color='yellow', 	img_src='/static/images/karlstad.jpg')
db.session.add(u)
u = models.User(name='Håkon', nickname='Haagon', 	number_of_beers=35,  about_me='Æ spillår trommer!', 		button_color='red', 	img_src='/static/images/haagon.jpg')
db.session.add(u)
u = models.User(name='Simen', nickname='Doktor', 	number_of_beers=7, 	 about_me='Eg skga bli doktor.', 		button_color='white', 	img_src='/static/images/simen.jpg')
db.session.add(u)
u = models.User(name='Vetle', nickname='Osterpus', 	number_of_beers=9, 	 about_me='E gårrr på madtegk', 		button_color='pink', 	img_src='/static/images/vetle.jpg')
db.session.add(u)
u = models.User(name='Magnus', nickname='Magga', 	number_of_beers=12,  about_me='Jeg flyr drone, ass!', 		button_color='green', 	img_src='/static/images/magnus.jpg')
db.session.add(u)
db.session.commit()

