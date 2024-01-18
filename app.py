import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

app = Flask(__name__)

 # SQLAlchemy Config
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from resources import (
    NewBookReource, GetAllBooksResource, GetBookResource, DeleteBooksResource, UpdateBookResource
)

api.add_resource(NewBookReource, '/books')
api.add_resource(GetAllBooksResource, '/books')
api.add_resource(GetBookResource, '/book/<int:book_id>/')
api.add_resource(DeleteBooksResource, '/book/<int:book_id>/')
api.add_resource(UpdateBookResource, '/book/<int:book_id>/')

# Index
@app.route('/') 
def index():
    return 'Welcome To My API'

