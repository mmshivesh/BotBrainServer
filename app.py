from flask import Flask, request, jsonify
import firebase
import math
app = Flask(__name__)

config = {
	'apiKey': "AIzaSyCsGSFbUuxCBzYLntqVkMMo598HGLGindc",
    'authDomain': "pdpapp-foresight.firebaseapp.com",
    'databaseURL': "https://pdpapp-foresight.firebaseio.com",
    'storageBucket': "pdpapp-foresight.appspot.com"
}

obj = ['L','R','R','S','H']

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
	app.run()