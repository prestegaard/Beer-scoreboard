#!flask/bin/python
from app import app, socketio

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 33507))
	#app.run(host='0.0.0.0', debug=True, threaded=True, port=port)
	socketio.run(app, debug=True, port=port)

