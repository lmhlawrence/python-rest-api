import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

	#save the json submission using parser
	parser = reqparse.RequestParser()
	parser.add_argument ('username',
		type=str,
		required=True,
		help="This field cannot be blank."
	)
	parser.add_argument ('password',
		type=str,
		required=True,
		help="This field cannot be blank."
	)

	def post(self):
		#use the json submission to add into database
		data = UserRegister.parser.parse_args()

		#ensures the user doesn't already exist
		if UserModel.find_by_username(data['username']):
			return {"message": "A user with that username already exists"}, 400

		#for each keys in data, pass it on
		user = UserModel(**data)
		user.save_to_db()

		return {"message": "User created successfully."}, 201
