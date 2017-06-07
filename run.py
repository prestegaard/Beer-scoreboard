#!flask/bin/python
from app import app, socketio

app.run(host='0.0.0.0', debug=True, threaded=True)

#socketio.run(app, debug=True)

