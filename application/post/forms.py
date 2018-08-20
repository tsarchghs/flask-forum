from wtforms import Form,StringField,validators

class PostForm(Form):
	content = StringField("content",[validators.required()])