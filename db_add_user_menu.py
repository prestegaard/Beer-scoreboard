#!flask/bin/python
from app import db, models
import datetime
from datetime import *

date                = 0
time                = 0
before              = 0
correckt_input      = 0
delete_hour_start   = 0
delete_minute_start = 0
delete_hour_end     = 0
delete_minute_end   = 0
date_for_print      = ''


def main():
    print("#### ADD NEW USER TO DATABASE ###" )
    print ("############################")
    u = models.User(name='Dummy', nickname='Dummy',      about_me='Lorem Ipsum!',  button_color='yellow',  img_src='/static/images/dahls.png')
    print("User name: ")
    tmp = str(input())
    if tmp:
        u.name = str(input())
    print("User nickname: ")
    tmp = str(input())
    if tmp:
        u.nickname = str(input())
    print("User about me: ")
    tmp = str(input())
    if tmp:
        u.about_me = str(input())
    print("User color: [red, blue, pink, green, white, yellow]: ")
    tmp = str(input())
    if tmp:
        u.button_color = str(input())
    print("Image: [name.jpg]")
    tmp = str(input())
    if tmp:
        u.img_src = '/static/images/' + str(input())

    print("Are you sure? : [Y/N]")
    answer = input()
    
    if(answer == 'Y'):

      
        u.location = 'Guests'
        db.session.add(u)
        db.session.commit()
    
    else:
        print('ERROR: CANCELED')
        print("db.session.commit() is done, beer list updated")
    

    beers = models.Beer.query.all()
    users = models.User.query.all()

    # Add location on user

    
    print ("############################")
    print ("Status overview of all users")
    for u in users:
        number_of_beers = 0
        for b in beers:
            if b.user_id == u.id:
                number_of_beers += 1
        print("ID: {}\t {}\t {}\t Beers: {}\t {}\t".format(u.id, u.name, u.nickname, number_of_beers, u.button_color).expandtabs(13) + "{}\t {}\t".format(u.about_me, u.location).expandtabs(30))
    print ("############################")



if __name__ == '__main__':
    main()