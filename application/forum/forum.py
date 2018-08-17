from flask import Blueprint, render_template,redirect,request,url_for,abort
from flask_login import current_user,login_required
from application.category.models import Category
from .forms import ForumForm
from .models import Forum
from .models import db as forum_db
from slugify import slugify
from application.thread.models import Thread

forum = Blueprint('forum', __name__,template_folder="templates/forum")

@forum.route("/<string:forum_slug>")
def showForum(forum_slug):
	forum = Forum.query.filter_by(slug=forum_slug).first()
	if not forum:
		abort(404)
	forum_threads = Thread.query.filter_by(forum_id=forum.id).all()
	return render_template("showForum.html",
							forum=forum,
							forum_threads=forum_threads)

@forum.route("/create/<string:category_slug>",methods=["GET","POST"])
@login_required
def createForum(category_slug):
	category = Category.query.filter_by(slug=category_slug).first()
	if not current_user.account_type == "administrator":
		abort(401)
	elif not category:
		abort(404)
	form = ForumForm(request.form)
	if request.method == "GET":
		return render_template("createForum.html",form=form)
	elif request.method == "POST":
		if not form.validate():
			return render_template("createForum.html",form=form)
		elif Forum.query.filter_by(name=form.name.data).all():
			return render_template("createForum.html",form=form,name_taken=True)
		forum = Forum(category_id=category.id,
					  name=form.name.data,
					  description=form.description.data)
		forum_db.session.add(forum)
		forum_db.session.commit()
		return redirect("/")

@forum.route("/edit/<string:forum_slug>",methods=["GET","POST"])
@login_required
def editForum(forum_slug):
	forum = Forum.query.filter_by(slug=forum_slug).first()
	if not current_user.account_type == "administrator":
		abort(401)
	elif not forum:
		abort(404)
	form = ForumForm(request.form)
	if request.method == "GET":
		return render_template("editForum.html",form=form,forum=forum)
	elif request.method == "POST":
		if not form.validate():
			return render_template("editForum.html",form=form,forum=forum)
		elif form.name.data != forum.name:
			if Forum.query.filter_by(name=form.name.data).all():
				return render_template("editForum.html",form=form,forum=forum,name_taken=True)
		forum.name = form.name.data
		forum.slug = slugify(form.name.data)
		forum.description = form.description.data
		forum_db.session.commit()
		return redirect("/")

@forum.route("/delete/<string:forum_slug>",methods=["GET","POST"])
@login_required
def deleteForum(forum_slug):
	forum = Forum.query.filter_by(slug=forum_slug).first()
	if not current_user.account_type == "administrator":
		abort(401)
	elif not forum:
		abort(404)
	if request.method == "GET":
		return render_template("delete_forum_confirmation.html",forum=forum)
	elif request.method == "POST":
		forum_db.session.delete(forum)
		forum_db.session.commit()
		return redirect(url_for("index"))
