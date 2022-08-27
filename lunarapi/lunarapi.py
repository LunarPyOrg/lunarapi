from flask import Flask
from flask_restful import Api, Resource
import random

def init(*, Appname: str, DataInput: list or str, Debug: bool = False, Randomic: bool = False, URL: str):
	app = Flask(Appname)
	api = Api(app)

	class DataList(Resource):
		def get(self):
			if Randomic == True:
				return random.choice(DataInput)
			else:
				return DataInput

	api.add_resource(DataList, URL)

	app.run(debug=Debug)

