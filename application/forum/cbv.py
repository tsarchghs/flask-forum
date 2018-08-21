from flask import request,abort,render_template,redirect,url_for
from flask.views import MethodView
from flask_login import login_required,current_user
from application.cbv import CreateView
from .models import Forum
from .models import db as forum_db
from .forms import ForumForm
from application.category.models import Category

class CreateForum(CreateView):
	def __init__(self,**kwargs):
		self.decorators = [login_required]
		self.template_name = "createForum.html"
		self.form = ForumForm
		self.model = Forum
		self.db = forum_db
		self.redirect_url = "forum.showForum"

	def get_post_redirect_args(self,model_instance):
		return {"forum_slug":model_instance.slug}

	def create_model_instance(self,form,**kwargs):
		category = Category.query.filter_by(slug=request.view_args["category_slug"]).first()
		print(request.view_args["category_slug"])
		print(category)
		if not category:
			abort(404)
		return self.model(category.id,
						  form.name.data,
						  form.description.data)