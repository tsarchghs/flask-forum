from flask import render_template
from application import app
from application.category.models import Category
from application.forum.models import Forum
from collections import OrderedDict

@app.route("/")
def index():
    categories = Category.query.all()
    category_forums = OrderedDict()
    for category in categories:
    	category_forums[category] = Forum.query.filter_by(category_id=category.id).all()
    return render_template("index.html",category_forums=category_forums)
