from flask import Flask
from application.authentication.auth import auth
import os

app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(auth, url_prefix='/auth')