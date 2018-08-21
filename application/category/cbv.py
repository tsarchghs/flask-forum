from flask import request,abort,render_template,redirect,url_for
from flask.views import MethodView
from flask_login import login_required,current_user
from .models import Category
from .forms import CategoryForm
from .models import db as category_db
from application.cbv import CreateView

"""class CreateCategory(MethodView):
	decorators = [login_required]
	template_name = "createCategory.html"
	form = CategoryForm
	db = category_db

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
		category = Category(form.name.data)
		self.db.session.add(category)
		self.db.session.commit()
		return redirect(url_for("category.showCategory",slug=category.slug))
"""

class CreateCategory(CreateView):
	def __init__(self):
		self.decorators = [login_required]
		self.template_name = "createCategory.html"
		self.form = CategoryForm
		self.model = Category
		self.db = category_db
		self.redirect_url = "category.showCategory"

	def get_post_redirect_args(self,model_instance):
		#return url_for("category.showCategory",category_slug=)
		return {"slug":model_instance.slug}