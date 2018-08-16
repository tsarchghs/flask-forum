from flask import Blueprint, render_template,redirect,request,url_for

category = Blueprint("category",
					 __name__,
					 template_folder="templates/category")

@category.route("/")
def showCategory():
	pass