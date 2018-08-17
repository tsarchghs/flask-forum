from flask_sqlalchemy import SQLAlchemy
from slugify import slugify

db = SQLAlchemy()

class Category(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String)
	slug = db.Column(db.String)

	def __init__(self,name):
		self.name = name
		self.slug =  slugify(name)

	def __repr__(self):
		return f"<Category {self.id}>"