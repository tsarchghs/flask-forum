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

@category.route("/edit/<slug>",methods=["GET","POST"])
@login_required
def editCategory(slug):
	category = Category.query.filter_by(slug=slug).first()
	if not category:
		abort(404)
	if current_user.account_type != "administrator":
		abort(401)
	form = CategoryForm(request.form,category)
	if request.method == "GET":
		return render_template("editCategory.html",form=form)
	else:
		if request.method == "POST":
			if not form.validate():
				return render_template("createCategory.html",form=form)
			category.name = form.name.data
			category.slug = slugify(form.name.data)
			category_db.session.commit()
			return redirect(url_for("category.showCategory",slug=category.slug))

@category.route("/delete/<slug>",methods=["GET","POST"])
@login_required
def deleteCategory(slug):
	category = Category.query.filter_by(slug=slug).first()
	if not category:
		abort(404)
	if current_user.account_type != "administrator":
		abort(401)
	if request.method == "GET":
		return render_template("delete_category_confirmation.html",category=category)
	elif request.method == "POST":
		category_db.session.delete(category)
		category_db.session.commit()
		return redirect("/index")