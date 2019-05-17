from flask_mongoengine import MongoEngine

db = MongoEngine()

def init_ext(app):
	db.init_app(app)
