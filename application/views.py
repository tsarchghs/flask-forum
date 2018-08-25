from flask import render_template
from application import app
from application.category.models import Category
from application.forum.models import Forum
from application.thread.models import Thread
from application.thread.models import db as thread_db
from collections import OrderedDict

@app.route("/")
def index():
    categories = Category.query.all()
    category_forums_threads = OrderedDict()
    for category in categories:
        forum_threads = OrderedDict()
        category_forums = Forum.query.filter_by(category_id=category.id).all()
        for forum in category_forums:
            threads = Thread.query.filter_by(forum_id=forum.id).all()
            forum_threads[forum] = threads
        category_forums_threads[category] = forum_threads
    return render_template("index.html",category_forums_threads=category_forums_threads)


