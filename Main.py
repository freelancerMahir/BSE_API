from flask import Flask
from flask_restful import Api,Resource,reqparse
from flask_cors import CORS
from others import share_prices

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

BSE_req = reqparse.RequestParser()
BSE_req.add_argument("Name", type=str, help="Name of the Company")

class BSE_CLASS(Resource):
	def get(self):
		return {"Data": share_prices()}
	def post(self):
		return {"Data": share_prices(name = BSE_req.parse_args()["Name"])}

api.add_resource(BSE_CLASS, "/")

if __name__ == "__main__":
	app.run(debug=True)