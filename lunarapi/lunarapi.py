from flask import Flask
from flask_restful import Api, Resource
import random

def init(name, data, *, Debug: bool = False, Randomic: bool = False):
	app = Flask(name)
	api = Api(app)

	class DataList(Resource):
		def get(self):
			if Randomic == True:
				return random.choice(data)
			else:
				return data

	api.add_resource(DataList, '/')

	app.run(debug=Debug)

