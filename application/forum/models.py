from flask_sqlalchemy import SQLAlchemy
from slugify import slugify
from application.category.models import Category

db = SQLAlchemy()

class Forum(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	category_id = db.Column(db.Integer,db.ForeignKey(Category.id))
	name = db.Column(db.String,unique=True)
	slug = db.Column(db.String,unique=True)
	description = db.Column(db.String)
	def __init__(self,name,description):
		self.name = name
		self.slug = slugify(name)
		self.description = self.description

