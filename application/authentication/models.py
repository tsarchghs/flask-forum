from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String,unique=True)
	email = db.Column(db.String,unique=True)
	password = db.Column(db.String)
	registered_on = db.Column('registered_on' , db.DateTime)
	account_type = db.Column(db.String)
	def __init__(self,username,email,password):
		self.username = username
		self.password = password
		self.email = email
		self.registered_on = datetime.utcnow()


	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

	def __repr__(self):
		return '<User %r>' % (self.username)