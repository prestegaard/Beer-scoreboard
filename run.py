#!flask/bin/python
from app import app, socketio

app.run(port=80, host='0.0.0.0', debug=True, threaded=True)

#socketio.run(app, debug=True)

