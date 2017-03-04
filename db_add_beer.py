#!flask/bin/python
from app import db, models
import datetime
from datetime import *

date               = 0
time               = 0
before             = 0
correckt_input     = 0
drink_hour_start   = 0
drink_minute_start = 0
drink_hour_end     = 0
drink_minute_end   = 0
date_for_print     = ''


def main():
    print("#### ADD BEER TO DATABASE ###" )

    print("drink how many days ago? [0 - 7]")
    days_ago = input()
    if(int(days_ago) >= 0 and int(days_ago) <= 7):
        date = datetime.today() - timedelta(int(days_ago))
    elif(int(days_ago) > 7):
        print('ERROR: TOO LONG AGO!')
        return 
    else:
        print('ERROR: WRONG DATE, MUST BE TODAY OR YESTERDAY')
        return 
    
    date_for_print = date.date().strftime('%a, %d %B %y')
    print("Selected: {}".format(date_for_print))

    timeformat = "%H.%M"
    
    print("Start drink time? [HH.MM]")
    time_input_start = input()    
    try:
        validtime = datetime.strptime(time_input_start, timeformat)
        #Do your logic with validtime, which is a valid format
    except ValueError:
        #Do your logic for invalid format (maybe print some message?).
        print('ERROR: WRONG TIME INPUT, MUST AA.BB OR YOU ARE OF OF BOUNDS')
        return 
         
    
    time_split_start    = time_input_start.split('.')
    drink_hour_start   = time_split_start[0]
    drink_minute_start = time_split_start[1]
    

    dummy = datetime.today()
    start_time = dummy.replace(hour=int(drink_hour_start), minute=int(drink_minute_start), second=0, microsecond=0)

    print("Selected time: {} , date: ".format(start_time.time(), date.date()))

    print("Choose specific user, or all users: [1-6]")
    user_input = input()
    if(int(user_input) >= 1 and int(user_input) <= 6):
        print("Are you sure? : [Y/N]")
        answer = input()
        u = models.User.query.get(int(user_input))

        beers = models.Beer.query.all()
        number_of_beers = 0
        for b in beers:
            if(b.drinker == u):
                number_of_beers += 1

        b = models.Beer(drinker=u, timestamp=start_time, beer_number=number_of_beers+1)
        db.session.add(b)
        db.session.commit()
        print("ADDED: Drinker: {}\t Timestamp: {}\t".format(b.drinker, b.timestamp).expandtabs(20))
        print("db.session.commit() is done, beer list corrected")
    else:
        print('ERROR: CANCELED')

if __name__ == '__main__':
    main()