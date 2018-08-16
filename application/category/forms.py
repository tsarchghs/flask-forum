from wtforms import Form, StringField, validators

class CategoryForm(Form):
	name = StringField("Category name:",
						[validators.DataRequired(message="Category name field is required!")])
