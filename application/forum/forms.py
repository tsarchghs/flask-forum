from wtforms import Form, StringField, validators

class ForumForm(Form):
	name = StringField("Forum name:",
						[validators.DataRequired(message="Category name field is required!")])
	description = StringField("Forum description:",
						[validators.DataRequired(message="Forum description field is required!")])
