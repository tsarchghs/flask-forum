from flask import redirect,url_for,abort,render_template,request
from flask_login import login_required,current_user
from flask.views import MethodView

class CreateView(MethodView):
	def __init__(self,decorators,template_name,form,model,db):
		self.decorators = decorators
		self.template_name = template_name
		self.form = form
		self.model = model
		self.db = db

	def get(self):
		form = self.form(request.form)
		if current_user.account_type != "administrator":
			abort(401)
		return render_template(self.template_name,form=form)

	def post(self):
		form = self.form(request.form)
		if current_user.account_type != "administrator":
			abort(401)
		if not form.validate():
			return render_template(self.template_name,form=form)
		model_instance = self.model(form.name.data)
		self.db.session.add(model_instance)
		self.db.session.commit()
		return redirect(url_for("category.showCategory",slug=model_instance.slug))
