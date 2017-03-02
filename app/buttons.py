from flask import Flask, render_template, redirect, url_for, session, escape, request
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid, socketio
from .models import User
import datetime

# Start with a basic flask app webpage.
#from flask.ext.socketio import SocketIO, emit
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()



    
# Imports for buttons
import RPi.GPIO as GPIO
import time
from enum import Enum

class UserButton(Enum):
    Vegard   = 25
    Karlstad = 24
    Haagon   = 23
    Simen    = 18
    Vetle    = 15
    Magga    = 14

class UserNumber(Enum):
    Vegard   = 1
    Karlstad = 2
    Haagon   = 3
    Simen    = 4
    Vetle    = 5
    Magga    = 6


GPIO.setmode(GPIO.BCM)

GPIO.setup(UserButton.Vegard.value,   GPIO.IN) 
GPIO.setup(UserButton.Karlstad.value, GPIO.IN) 
GPIO.setup(UserButton.Haagon.value,   GPIO.IN) 
GPIO.setup(UserButton.Simen.value,    GPIO.IN)
GPIO.setup(UserButton.Vetle.value,    GPIO.IN)
GPIO.setup(UserButton.Magga.value,    GPIO.IN)

# for GPIO interrupts
#RPIO.add_interrupt_callback(7, do_something, threaded_callback=True)
#GPIO.add_event_detect(24, GPIO.RISING, callback=my_callback)

class RandomThread(Thread):
    def __init__(self):
        self.delay = 1
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        users = User.query.all()
        print ("Making random numbers")
        while not thread_stop_event.isSet():
#            number = round(random()*10, 3)
#            print (number)
#            socketio.emit('newnumber', {'number': number}, namespace='/test')
            number =  ' Drinks a beer!'
#            socketio.emit('user_socket', {'number': number}, namespace='/test')
            sleep(self.delay*1000)
            
    def run(self):
        self.randomNumberGenerator()






 
def buttonPressed(user_number):
    user = User.query.get(user_number)
    # Debug print
    print ("{} \tdrank a beer!".format(user.nickname)) 
    # Increment number of beers
    number_of_beers = user.number_of_beers
    number_of_beers = number_of_beers +1
    now = datetime.datetime.now()
    # Update user, and save current changes to database
    user.number_of_beers = number_of_beers
    user.last_seen = now.strftime("%Y-%m-%d %H:%M:%S")
    db.session.commit()
    
    # Create message to send
    msg = { 'nickname': str(user.nickname), 
            'number_of_beers': str(user.number_of_beers),
            'last_seen_on': str(user.last_seen)
            }
    
    socketio.emit('nickname socket', {'data': str(user.nickname)}, namespace='/test')
    sleep(0.01)
    socketio.emit('beer socket', {'data': str(user.number_of_beers)}, namespace='/test')
    sleep(0.01)
    socketio.emit('last seen socket', {'data': str(user.last_seen)}, namespace='/test')
    sleep(0.01)
    
    # Did not work 'users socket'
    #socketio.emit('user socket', data=(user.nickname, user.number_of_beers, user.last_seen_on), namespace='/test') 

    # Update client side with the new number of beers
    '''
    users = User.query.all()
    for user in users:
        number = user.nickname + ': ' + str(user.number_of_beers)
        socketio.emit('newnumber', {'number': number}, namespace='/test')
'''

GPIO.add_event_detect(UserButton.Vegard.value,   GPIO.RISING,  callback=lambda x: buttonPressed(UserNumber.Vegard.value),   bouncetime=2000)
GPIO.add_event_detect(UserButton.Karlstad.value, GPIO.RISING,  callback=lambda x: buttonPressed(UserNumber.Karlstad.value), bouncetime=2000)
GPIO.add_event_detect(UserButton.Haagon.value,   GPIO.RISING,  callback=lambda x: buttonPressed(UserNumber.Haagon.value),   bouncetime=2000)
GPIO.add_event_detect(UserButton.Simen.value,    GPIO.RISING,  callback=lambda x: buttonPressed(UserNumber.Simen.value),    bouncetime=2000)
GPIO.add_event_detect(UserButton.Vetle.value,    GPIO.RISING,  callback=lambda x: buttonPressed(UserNumber.Vetle.value),    bouncetime=2000)
GPIO.add_event_detect(UserButton.Magga.value,    GPIO.RISING,  callback=lambda x: buttonPressed(UserNumber.Magga.value),    bouncetime=2000)

print ("Buttons are initialized")


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')
   
    users = User.query.all()
    for user in users:    
        socketio.emit('nickname socket', {'data': str(user.nickname)}, namespace='/test')
        sleep(0.01)
        socketio.emit('beer socket', {'data': str(user.number_of_beers)}, namespace='/test')
        sleep(0.01)
        socketio.emit('last seen socket', {'data': str(user.last_seen)}, namespace='/test')
        sleep(0.01)

    #Start the random number generator thread only if the thread has not been started before.
 #   if not thread.isAlive():
 #       print ("Starting Thread")
 #       thread = RandomThread()
 #       thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')



'''
if __name__ == '__main__':
    socketio.run(app)
    print ("NOW I AM AT END OF APP.PY INSIDE MAIN")
'''