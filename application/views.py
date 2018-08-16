from flask import render_template
from application import app
from application.category.models import Category

@app.route("/")
def index():
    categories = Category.query.all()
    return render_template("index.html",categories=categories)
