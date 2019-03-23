from flask import Flask, request, jsonify
import json
from datetime import datetime
import math
app = Flask(__name__)

## Get Json objects

with open("json/error.json") as error_file:
	error = json.load(error_file)
with open("json/database.json") as data_file:
	lists = json.load(data_file)


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return f"<h1>~PDP Server~</h1><p>Time: {the_time}.</p> <p>Version: 0.1</p><p>Build: 12</p>"

@app.route('/lists')
def returnlists():
	list_len = len(lists)
	try:	# as long as the id is not NoneType
		i = int(request.args.get('id'))
		if(i<list_len):
			return jsonify(lists[i])
		else:
			return jsonify(error)
	except:	# If there is no id
		temp = {"no_of_lists":list_len}
		return jsonify(temp)

if __name__=='__main__':
	app.run(debug=True, use_reloader=True)