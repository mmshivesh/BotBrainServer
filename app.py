from flask import Flask, request, jsonify
from datetime import datetime
import math
app = Flask(__name__)

sample_obj = ['L','R','R','S','H']

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello PDP!</h1>
    <p>It is currently {time}.</p>
    """.format(time=the_time)

@app.route('/getpath')
def getpath():
	# request.args.get("<query-param>")
	return jsonify(sample_obj)

if __name__=='__main__':
	app.run(debug=True, use_reloader=True)