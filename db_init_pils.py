#!flask/bin/python
from app import db, models
import datetime
users = models.User.query.all()
beers = models.Beer.query.all()
number_of_beers = 0

# Add location on user
for u in users:
    if u.id <= 5 or u.id == 7:
        u.location = 'Criben'
    elif u.id == 6 or u.id == 9:
        u.location = 'VIPs'
    else:
        u.location = 'Guests'
    db.session.add(u)
db.session.commit()



# Delete all users
'''
for u in users:
	db.session.delete(u)
db.session.commit()
'''
# Delete beers
'''
for b in beers:
    if b.id > 69:
        db.session.delete(b)
db.session.commit() 
'''
'''
u = models.User(name='Vegard', nickname='Laowi', 	 about_me='Eg e ein Revolveman.', 		button_color='blue', 	img_src='/static/images/vegard.jpg')
db.session.add(u)
u = models.User(name='Øyvind', nickname='Karlstad',  about_me='Je et flesk og pannkak.', 	button_color='yellow', 	img_src='/static/images/karlstad.jpg')
db.session.add(u)
u = models.User(name='Håkon', nickname='Haagon', 	 about_me='Æ spillår trommer!', 		button_color='red', 	img_src='/static/images/haagon.jpg')
db.session.add(u)
u = models.User(name='Simen', nickname='Doktor', 	 about_me='Eg skga bli doktor.', 		button_color='white', 	img_src='/static/images/simen.jpg')
db.session.add(u)
u = models.User(name='Vetle', nickname='Osterpus', 	 about_me='E gårrr på madtegk', 		button_color='pink', 	img_src='/static/images/vetle.jpg')
db.session.add(u)
u = models.User(name='Magnus', nickname='Magga', 	 about_me='Jeg flyr drone, ass!', 		button_color='green', 	img_src='/static/images/magnus.jpg')
db.session.add(u)
db.session.commit()
'''
# Initialize full database

# Delete specific user
'''
for u in users:
    if u.name == 'Rune':
        db.session.delete(u)
'''

# Add specific user
'''
u = models.User(name='Gunnar', nickname='Gummy', 	 about_me='Kommersielle helvette!', 	button_color='red', 	img_src='/static/images/gunnar.jpg')
db.session.add(u)
db.session.commit()
'''

# Change info on specific user
'''
karlstad = models.User.query.get(2)
karlstad.about_me = 'Je har kjøpt leilighet'
karlstad.button_color= 'green'


db.session.add(karlstad)
db.session.commit()
'''

