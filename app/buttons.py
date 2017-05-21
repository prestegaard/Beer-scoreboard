
from app import app, db, socketio
from .models import User
from .models import Beer
import datetime
from datetime import *
from time import sleep
from random import randint
import time
from enum import Enum
import platform

COMMIT_TO_DB = False

sysname = platform.system()
sysrel = platform.release()
sysver = platform.version()

print(sysname + " " + sysver + " " )

if 'Ubuntu' in sysver:
    TEST_ON_LAPTOP = True
    print("Testing on laptop")

# Imports for buttons
else:
    TEST_ON_LAPTOP = False
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)

last_press = time.time()
buttons_initialized = 0
thread = None



class UserButton(Enum):
    Vegard   = 25 # Blue
    Rune     = 24 # Yellow
    Haagon   = 23 # Red
    Simen    = 18 # White
    Vetle    = 15 # Pink
    Karlstad = 14 # Green

class UserNumber(Enum):
    Vegard   = 1
    Karlstad = 2
    Haagon   = 3
    Simen    = 4
    Vetle    = 5
    Magga    = 6
    Rune     = 7




def buttonPressed(user_pin, user_number): 
    global last_press

    button_is_truly_pressed_flag = 0 
    print ("RIGSING BUTTON DETECTED, PIN: {}".format(user_pin))
    now = time.time()
    if now - last_press < 2:
        print("NOT ENGOUGH TIME FROM LAST RISING BUTTON\n")
        return

    timeout = time.time() + 0.200   # 200 milliseconds from now
    time.sleep(0.05)
    while(GPIO.input(user_pin) == True):
        #print("INSIDE WHILE LOOP")
        time.sleep(0.001)    
        if time.time() > timeout:
            button_is_truly_pressed_flag = 1
            print ("MORE THAN ENGOUGH PRESS TIME ON BUTTON, beer approved!\n")
            break

    if (not button_is_truly_pressed_flag):
        rising_time = time.time()
        print("RETURN, TOO SHORT PRESS. Only {}\t s long press. Time is now: {}\n".format(rising_time-now, now.time))
        return      

     # Update last approved beer
    last_press = now
    # Update database
    update_beer_cnt(user_number)
    # Update web page
    update_web_page_single_user_info(user_number)
    update_web_page_with_sound()

def update_beer_cnt(user_number):
    # Content here is somewhat equal to content of db_add_beer.py
    user = User.query.get(user_number)
    beers = Beer.query.all()

    number_of_beers = 0
    for b in beers:
        if(b.drinker == user):
            number_of_beers += 1
    
    b = Beer(drinker=user, timestamp=datetime.now(), beer_number=number_of_beers+1)
    db.session.add(b)
    if COMMIT_TO_DB == True:
        db.session.commit()
    print ("### {}\t : drank beer number {}\t###".format(user.nickname, b.beer_number).expandtabs(10)) 


def update_web_page_with_sound():
    sound_number = randint(1, 14)  # Integer, endpoints included
    socketio.emit('play sound socket', {'data': str(sound_number)}, namespace='/test')
    sleep(0.01)
    print("Sound number: {}".format(sound_number))


def update_web_page_single_user_info(user_number):
    user = User.query.get(user_number)
    beers = Beer.query.all()

    number_of_beers = 0
    last_seen = datetime.now() # Dummy to get correct data type
    for b in beers:
        if(b.drinker == user):
            number_of_beers = b.beer_number
            last_seen = b.timestamp

    last_seen = last_seen.strftime("%Y-%m-%d %H:%M:%S")
    if(number_of_beers == 0 ):
        number_of_beers = 'none'
        last_seen = 'never'
    # Create message to send
    msg = { 'nickname': str(user.nickname), 
            'number_of_beers': str(number_of_beers),
            'last_seen_on': str(last_seen)
            }
    
    socketio.emit('nickname socket', {'data': str(user.nickname)}, namespace='/test')
    sleep(0.01)
    socketio.emit('beer socket', {'data': str(number_of_beers)}, namespace='/test')
    sleep(0.01)
    socketio.emit('last seen socket', {'data': str(last_seen)}, namespace='/test')
    sleep(0.01)
    
    print("WEBPAGE UPDATED")
    # Did not work 'users socket'
    #socketio.emit('user socket', data=(user.nickname, user.number_of_beers, user.last_seen_on), namespace='/test') 

    # Update client side with the new number of beers
    '''
    users = User.query.all()
    for user in users:
        number = user.nickname + ': ' + str(user.number_of_beers)
        socketio.emit('newnumber', {'number': number}, namespace='/test')   
'''
def buttons_init():
    GPIO.setup(UserButton.Vegard.value,   GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(UserButton.Karlstad.value, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(UserButton.Haagon.value,   GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
    GPIO.setup(UserButton.Simen.value,    GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(UserButton.Vetle.value,    GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(UserButton.Rune.value,     GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    GPIO.add_event_detect(UserButton.Vegard.value,   GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Vegard.value,   UserNumber.Vegard.value),      bouncetime=200)
    GPIO.add_event_detect(UserButton.Karlstad.value, GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Karlstad.value, UserNumber.Karlstad.value),    bouncetime=200)
    GPIO.add_event_detect(UserButton.Haagon.value,   GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Haagon.value,   UserNumber.Haagon.value),      bouncetime=200)
    GPIO.add_event_detect(UserButton.Simen.value,    GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Simen.value,    UserNumber.Simen.value),       bouncetime=200)
    GPIO.add_event_detect(UserButton.Vetle.value,    GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Vetle.value,    UserNumber.Vetle.value),       bouncetime=200)
    GPIO.add_event_detect(UserButton.Rune.value,     GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Rune.value,     UserNumber.Rune.value),        bouncetime=200)
    #GPIO.add_event_detect(UserButton.Magga.value,    GPIO.RISING,  callback=lambda x: buttonPressed(UserButton.Magga.value,    UserNumber.Magga.value),       bouncetime=200)
    print ("Buttons are initialized")

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


@socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected')
    # Must initialize buttons once. This happens when first client connects
    global buttons_initialized
    if not buttons_initialized:
        if TEST_ON_LAPTOP == False:
            buttons_init()
        buttons_initialized = 1

    # Thread that simulates button presses when testing on laptop
    if TEST_ON_LAPTOP == True:
        global thread
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)

    last_seen_user = User.query.get(1)

    users = User.query.all()
    beers = Beer.query.all()

    for user in users:
        update_web_page_single_user_info(user.id)
    # Get latest drinker on page refresh
    for beer in beers:
        last_seen_user = beer.drinker
    update_web_page_single_user_info(last_seen_user.id)

# Thread to simulate button presses every tenth second.
def background_thread():
    print ("Starting for loop")
    i = 0
    j = 0
    for i in range (1,8):
        for j in range (0, 10):
            update_beer_cnt(i)
            update_web_page_single_user_info(i)
            update_web_page_with_sound()
            print("Message sent from for loop: {}".format(i))
            socketio.sleep(2)



'''
if __name__ == '__main__':
    socketio.run(app)
    print ("NOW I AM AT END OF APP.PY INSIDE MAIN")
'''
