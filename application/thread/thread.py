from flask import Blueprint,abort,request,render_template,url_for,redirect
from flask_login import current_user,login_required
from application.forum.models import Forum
from .forms import ThreadForm
from .models import db as thread_db
from .models import Thread

thread = Blueprint("thread",__name__,
					template_folder="templates/thread")

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
						description=form.description.data)
		thread_db.session.add(thread)
		thread_db.session.commit()
		return redirect("/showThread")