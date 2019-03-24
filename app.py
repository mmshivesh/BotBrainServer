from flask import Flask, request, jsonify
import json
from datetime import datetime
import math

#Algo imports
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.ida_star import IDAStarFinder
from src.bot import bot
from src.store import store

from src.status import status

app = Flask(__name__)

## Get Json objects

with open("json/error.json") as error_file:
	error = json.load(error_file)
with open("json/database.json") as data_file:
	lists = json.load(data_file)
with open("json/store.json") as store_data_file:
	store_dat = json.load(store_data_file)
with open("json/bot.json") as bot_data_file:
	bot_dat = json.load(bot_data_file)
with open("json/productMapping.json") as prod_map_file:
	prod_map = json.load(prod_map_file)
list_len = len(lists)
x = store(store_dat["schema"])
b1 = bot(bot_dat["1"]["pos"],bot_dat["1"]["dir"],store_dat["billing"])
end_points = []
response = ""
ready = False
cont = False
state = status(end_points,response,ready,cont)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return f"<h1>~PDP Server~</h1><p>Time: {the_time}.</p> <p>Version: 0.1</p><p>Build: 15</p>"

@app.route('/lists')
def returnlists():
	try:	# as long as the id is not NoneType
		i = int(request.args.get('id'))
		if(i<list_len):
			return jsonify(lists[i])
		else:
			return jsonify(error)
	except:	# If there is no id
		temp = {"no_of_lists":list_len}
		return jsonify(temp)

@app.route('/products')
def returnproducts():
	return jsonify(list(prod_map.keys()))

@app.route('/botNav')
def set_end_points():
	i = int(request.args.get('list'))
	if(i is not None):
		print(list)
		if(i<list_len):
			if(state.ready):
				return jsonify("Session Underway")
			else:
				item_list=lists[i]["items"]
				for item in item_list:
					state.end_points.append(prod_map[item])
				print(end_points)
				state.response = jsonify({"ready":True,"path":b1.command(x,end_points)})
				state.end_points = []
				state.ready = True
				print(state.response)
		else:
			return jsonify(error)
	else:
		return jsonify("BOT NAV")
	print(end_points)
	return jsonify("Follow Bot")

@app.route('/getPath')
def return_path():
	if(state.ready):
		return state.response
	else:
		return jsonify({"ready":False,"path":""})

@app.route('/endSession')
def endSes():
	state.ready = False
	state.response = ""
	state.end_points = []
	state.cont = False
	return jsonify("Successful")

@app.route('/botCont')
def chngbotstate():
	x = state.cont
	state.cont = False
	return jsonify({"S":x})

@app.route('/appCont')
def chngappState():
	state.cont = True
	return jsonify("Successful")

if __name__=='__main__':
	app.run(debug=True, use_reloader=True)