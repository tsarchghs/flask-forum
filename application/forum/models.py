from flask_sqlalchemy import SQLAlchemy
from slugify import slugify

db = SQLAlchemy()

class Forum(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String,unique=True)
	slug = db.Column(db.String,unique=True)
	description = db.Column(db.String)
	def __init__(self,name,description):
		self.name = name
		self.slug = slugify(name)
		self.description = self.description

