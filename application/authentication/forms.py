from wtforms import Form, BooleanField, StringField, PasswordField, validators

class LoginForm(Form):
	username = StringField('Username',
						[validators.DataRequired(message="Username field is required!")])
	password = StringField('Password',
							[validators.DataRequired(message="Password field is required!")])