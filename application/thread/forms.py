from wtforms import Form,StringField,TextField,validators

class ThreadForm(Form):
	title = StringField("Title",[validators.required(), validators.length(max=150)])
	description = TextField("description",[validators.required()])