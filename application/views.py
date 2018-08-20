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
    dict_ = OrderedDict()
    forum_threads = OrderedDict()
    for category in categories:
    	category_forums = Forum.query.filter_by(category_id=category.id).all()
    	for forum in category_forums:
    		thread_db_session = thread_db.session
    		forum_threads[forum] = thread_db_session.query(Thread.forum_id.in_([forum.id for forum in category_forums])).all()
    	dict_[category] = forum_threads
    return render_template("index.html",category_forums=dict_)
