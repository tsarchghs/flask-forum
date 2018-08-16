from flask import Blueprint, render_template,redirect,request,url_for,abort
from .models import Category

category = Blueprint("category",
					 __name__,
					 template_folder="templates/category")

@category.route("/<string:slug>")
def showCategory(slug):
	category = Category.query.filter_by(slug=slug).first()
	if not category:
		abort(404)
	return render_template("showCategory.html",category=category)