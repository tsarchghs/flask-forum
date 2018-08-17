from flask import Blueprint,abort,request,render_template,url_for,redirect
from flask_login import current_user,login_required
from application.forum.models import Forum
from .forms import ThreadForm
from .models import db as thread_db
from .models import Thread
from slugify import slugify

thread = Blueprint("thread",__name__,
					template_folder="templates/thread")

@thread.route("/<string:thread_slug>")
def showThread(thread_slug):
	thread = Thread.query.filter_by(slug=thread_slug).first()
	if not thread:
		abort(404)
	return render_template("showThread.html",thread=thread)
	

@thread.route("/create/<string:forum_slug>",methods=["GET","POST"])
@login_required
def createThread(forum_slug):
	forum = Forum.query.filter_by(slug=forum_slug).first()
	if not forum:
		abort(404)
	form = ThreadForm(request.form)
	if request.method == "GET":
		return render_template("createThread.html",form=form,forum=forum)
	elif request.method == "POST":
		if not form.validate():
			return render_template("createThread.html",form=form,forum=forum)
		thread = Thread(forum_id=forum.id,
						user_id=current_user.id,
						title=form.title.data,
						slug=slugify(form.title.data),
						description=form.description.data)
		thread_db.session.add(thread)
		thread_db.session.commit()
		return redirect("/showThread")

@thread.route("/edit/<string:thread_slug>",methods=["GET","POST"])
@login_required
def editThread(thread_slug):
	thread = Thread.query.filter_by(slug=thread_slug).first()
	if not thread:
		abort(404)
	elif not thread.user_id == current_user.id:
		abort(401)
	form = ThreadForm(request.form)
	if request.method == "GET":
		return render_template("editThread.html",form=form,thread=thread)
	elif request.method == "POST":
		if not form.validate():
			return render_template("editThread.html",form=form,thread=thread)
		thread.title = form.title.data
		thread.slug = slugify(form.title.data)
		thread.description = form.description.data
		thread_db.session.commit()
		return redirect(url_for("thread.showThread",thread_slug=thread.slug))

@thread.route("/delete/<string:thread_slug>",methods=["GET","POST"])
@login_required
def deleteThread(thread_slug):
	thread = Thread.query.filter_by(slug=thread_slug).first()
	if not thread:
		abort(404)
	elif not thread.user_id == current_user.id:
		abort(401)
	forum = Forum.query.get_or_404(thread.forum_id)
	if request.method == "GET":
		return render_template("delete_thread_confirmation.html",thread=thread)
	elif request.method == "POST":
		thread_db.session.delete(thread)
		thread_db.session.commit()
		return redirect(url_for("forum.showForum",forum_slug=forum.slug))