from flask import Blueprint, render_template,redirect,request,url_for
from .models import Category
category = Blueprint("category",
					 __name__,
					 template_folder="templates/category")

@category.route("/<int:ID>")
def showCategory(ID):
	category = Category.query.get_or_404(ID)
	return render_template("showCategory.html",category=category)