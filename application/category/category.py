from flask import Blueprint, request,render_template,abort,url_for,redirect
from flask_login import current_user,login_required
from .models import Category
from .models import db as category_db
from .forms import CategoryForm
from slugify import slugify

category = Blueprint("category",
					 __name__,
					 template_folder="templates/category")

@category.route("/<string:slug>")
def showCategory(slug):
	category = Category.query.filter_by(slug=slug).first()
	if not category:
		abort(404)
	return render_template("showCategory.html",category=category)

@category.route("/create",methods=["GET","POST"])
@login_required
def createCategory():
	if current_user.account_type != "administrator":
		abort(401)
	form = CategoryForm(request.form)
	if request.method == "GET":
		return render_template("createCategory.html",form=form)
	else:
		if request.method == "POST":
			if not form.validate():
				return render_template("createCategory.html",form=form)
			category = Category(form.name.data)
			category_db.session.add(category)
			category_db.session.commit()
			return redirect(url_for("category.showCategory",slug=category.slug))