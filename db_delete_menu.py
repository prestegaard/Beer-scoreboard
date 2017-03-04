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
    print("#### DELETE FROM DATABASE ###" )

    print("Delete how many days ago? [0 - 7]")
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
    
    print("Start delete time? [HH.MM]")
    time_input_start = input()    
    try:
        validtime = datetime.strptime(time_input_start, timeformat)
        #Do your logic with validtime, which is a valid format
    except ValueError:
        #Do your logic for invalid format (maybe print some message?).
        print('ERROR: WRONG TIME INPUT, MUST AA.BB OR YOU ARE OF OF BOUNDS')
        return 
         
    print("End delete time? [HH.MM]")
    time_input_end = input()    
    try:
        validtime = datetime.strptime(time_input_end, timeformat)
        #Do your logic with validtime, which is a valid format
    except ValueError:
        #Do your logic for invalid format (maybe print some message?).
        print('ERROR: WRONG TIME INPUT, MUST AA.BB OR YOU ARE OF OF BOUNDS')
        return      
    
    time_split_start    = time_input_start.split('.')
    delete_hour_start   = time_split_start[0]
    delete_minute_start = time_split_start[1]
    
    time_split_end      = time_input_end.split('.')
    delete_hour_end     = time_split_end[0]
    delete_minute_end   = time_split_end[1]

    dummy = datetime.today()
    start_time = dummy.replace(hour=int(delete_hour_start), minute=int(delete_minute_start), second=0, microsecond=0)
    end_time = dummy.replace(hour=int(delete_hour_end), minute=int(delete_minute_end), second=0, microsecond=0)

    print("Selected time: [{} <-> {}], date: ".format(start_time.time(), end_time.time(), date.date()))

    print("Choose specific user, or all users: [all] or [1-6]")
    user_input = input()

    print("Are you sure? : [Y/N]")
    answer = input()
    
    if(answer == 'Y'):

        beers = models.Beer.query.all()
        for b in beers:
            if(b.timestamp.date() == date.date()):
                    # Delete beer today, before given time
                    if(b.timestamp.time() >= start_time.time() and b.timestamp.time() <= end_time.time()):
                        if (user_input == 'all'):
                            db.session.delete(b)
                            print("DELETED: Drinker: {}\t Timestamp: {}\t".format(b.drinker, b.timestamp).expandtabs(20))
                        elif(int(user_input) >= 1 and int(user_input) <= 6):
                            u = models.User.query.get(int(user_input))
                            if(b.drinker == u):
                                 db.session.delete(b)
                                 print("DELETED: Drinker: {}\t Timestamp: {}\t".format(b.drinker, b.timestamp).expandtabs(20))

        db.session.commit()
        print("db.session.commit() is done, beer list corrected")

    
    else:
        print('ERROR: CANCELED')




if __name__ == '__main__':
    main()