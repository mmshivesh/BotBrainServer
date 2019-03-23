from flask import Flask, request, jsonify
from datetime import datetime
import math
app = Flask(__name__)

config = {
	'apiKey': "AIzaSyCsGSFbUuxCBzYLntqVkMMo598HGLGindc",
    'authDomain': "pdpapp-foresight.firebaseapp.com",
    'databaseURL': "https://pdpapp-foresight.firebaseio.com",
    'storageBucket': "pdpapp-foresight.appspot.com"
}

obj = ['L','R','R','S','H']

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

@app.route('/push')
def push():
	# return "Pushing element into the server"
	return jsonify(obj)


@app.route('/query')
def query():
	print(request.args.get('x'), request.args.get('y'))
	return "Querying the database"

if __name__=='__main__':
	# instance = firebase.Firebase(config)
	# database_i = instance.database()
	# print(database_i.child('root').get().val())	
	app.run(debug=True, use_reloader=True)