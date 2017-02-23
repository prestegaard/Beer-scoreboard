from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .models import User
import datetime



# Start with a basic flask app webpage.
#from flask.ext.socketio import SocketIO, emit
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
thread_stop_event = Event()


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
            for user in users:
                number = user.nickname + ': ' + str(user.number_of_beers)
                socketio.emit('newnumber', {'number': number}, namespace='/test')
                sleep(self.delay)

    def run(self):
        self.randomNumberGenerator()





@app.route('/')
@app.route('/index')
def index():
    user = "Haagon"
    beer = [  # fake array of posts
        { 
            'Drinker': {'nickname': 'Haagon'}, 
            'When':  datetime.datetime.utcnow().strftime("%A, %d. %B %Y %H:%M")

        },
        { 
            'Drinker': {'nickname': 'Susan'}, 
            'When': datetime.datetime.utcnow().strftime("%A, %d. %B %Y %H:%M")

        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           beer=beer)

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print ("Starting Thread")
        thread = RandomThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


@app.route('/toilet')
def toilet():
    return render_template("toilet.html")



@app.route('/users')
def users():
   # user = User.query.get(3)
    users = User.query.all()

#    posts = [
#        {'author': user, 'body': 'Test post #1'},
#        {'author': user, 'body': 'Test post #2'}
#    ]
    return render_template('user.html',
                           users=users
    #                       user=user,
    #                       posts=posts
                           )
@app.route('/users2')
def users2():
   # user = User.query.get(3)
    users = User.query.all()


    return render_template('user2.html',
                           users=users
                           )


if __name__ == '__main__':
    socketio.run(app)