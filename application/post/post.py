from flask import Blueprint,request,redirect,url_for,render_template
from application.thread.models import Thread
from application.post.models import Post
from application.post.models import db as post_db
from application.post.forms import PostForm
from flask_login import login_required,current_user

post = Blueprint("post",__name__,
				template_folder="templates/post")

@post.route("/create/<string:thread_slug>",methods=["GET","POST"])
@login_required
def createPost(thread_slug):
	thread = Thread.query.filter_by(slug=thread_slug).first()
	if not thread:
		abort(404)
	form = PostForm(request.form)
	if request.method == "GET":
		return render_template("createPost.html",form=form,thread=thread)
	elif request.method == "POST":
		if not form.validate():
			return render_template("createPost.html",form=form,thread=thread)
		post = Post(thread_id=thread.id,
					user_id=current_user.id,
					content=form.content.data)
		post_db.session.add(post)
		post_db.session.commit()
		return redirect(url_for("thread.showThread",thread_slug=thread_slug))
