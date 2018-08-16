from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String)
	def __repr__(self):
		return "<Category {self.id}"