import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
#turn the flask app into a socketio app
socketio = SocketIO(app)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models, buttons