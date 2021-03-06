import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#import methods authenticate and identity from security.py
from security import authenticate, identity

#import UserRegister class from user.py
from resources.user import UserRegister

#import classes from item.py file
from resources.item import Item, ItemList

#import stores from stores.py
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

#JWT creates a new endpoint called /auth
#JWT sends the username and password into authenticate
#If they match, /auth endpoint sends back a token
#Uses the token for the identity function
jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

#the file that is run is always assigned as '__main__'
if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)
