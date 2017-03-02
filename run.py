#!flask/bin/python
from app import app

app.run(port=5000, host='0.0.0.0', debug=True, threaded=True)
