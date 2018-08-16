from flask import Flask
from application.authentication.auth import auth,login_manager
from application.authentication.models import db as auth_db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/db.sqlite3'.format(str(os.getcwd()))
app.config.from_object(os.environ.get('SETTINGS'))

with app.app_context():
	login_manager.init_app(app)
	auth_db.init_app(app)
	auth_db.create_all()
app.register_blueprint(auth, url_prefix='/auth')