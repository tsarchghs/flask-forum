from flask import Flask
from application.authentication.auth import auth,login_manager
from application.category.category import category
from application.authentication.models import db as auth_db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////{}/db.sqlite3'.format(str(os.getcwd()))
app.config.from_object(os.environ.get('SETTINGS'))
app.secret_key = os.urandom(24)
with app.app_context():
	login_manager.init_app(app)
	auth_db.init_app(app)
	auth_db.create_all()
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(category,url_prefix="/category")