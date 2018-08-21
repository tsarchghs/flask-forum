from flask import redirect,url_for,abort,render_template,request
from flask_login import login_required,current_user
from flask.views import MethodView

class CreateView(MethodView):
	def __init__(self,decorators,template_name,form,model,db,url):
		self.decorators = decorators
		self.template_name = template_name
		self.form = form
		self.model = model
		self.db = db
		self.redirect_url = url

	def get_post_redirect_args(self,model_instance):
		raise NotImplementedError

	def create_model_instance(self,form):
		raise NotImplementedError

	def get(self,**kwargs):
		form = self.form(request.form)
		if current_user.account_type != "administrator":
			abort(401)
		return render_template(self.template_name,form=form)

	def post(self,**kwargs):
		form = self.form(request.form)
		if current_user.account_type != "administrator":
			abort(401)
		if not form.validate():
			return render_template(self.template_name,form=form)
		model_instance = self.create_model_instance(form)
		self.db.session.add(model_instance)
		self.db.session.commit()
		args = self.get_post_redirect_args(model_instance)
		return redirect(url_for(self.url,**args))

"""for field in self.model.__table__.columns:
args[model_instance.field] = form.field.data
model_instance = model(**args)"""