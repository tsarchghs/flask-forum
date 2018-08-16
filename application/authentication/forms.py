from wtforms import Form, BooleanField, StringField, validators
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
	username = StringField('Username',
						[validators.DataRequired(message="Username field is required!")])
	password = StringField('Password',
							[validators.DataRequired(message="Password field is required!")])

class RegisterForm(Form):
	username = StringField("Username",
							[validators.DataRequired(message="Username field is required!")])
	password = StringField("Password",
							[validators.DataRequired(message="Password field is required!")])
	email = EmailField("Email",
						[validators.DataRequired(message="Email field is required!"),
						validators.Email()])