from flask_sqlalchemy import SQLAlchemy
from application.forum.models import Forum

db = SQLAlchemy()

class Thread(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey(Forum.id))
	title = db.Column(db.String(150))
	description = db.Column(db.String)
	def __repr__(self):
		return f"<Thread {self.id}>"
		