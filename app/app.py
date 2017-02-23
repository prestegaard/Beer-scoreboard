from flask import Flask, render_template, redirect, url_for, session, escape, request
from flask_socketio import SocketIO, emit


app = Flask(__name__)


'''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
'''

'''
if __name__ == '__main__':
    socketio.run(app)
'''