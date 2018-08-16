
from flask import Blueprint, render_template
from flask_login import LoginManager, UserMixin, login_required,current_user,login_user,logout_user
from .models import User

auth = Blueprint('auth', __name__,template_folder="templates/auth")
login_manager = LoginManager()

@login_manager.user_loader
def load_user(ID):
	return User.query.get(ID)

@auth.route('/login')
def login():
    return render_template('login.html')
