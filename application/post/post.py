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
	post_form = PostForm(request.form)
	if request.method == "GET":
		return render_template("createPost.html",post_form=post_form,thread=thread)
	elif request.method == "POST":
		if not post_form.validate():
			return render_template("createPost.html",post_form=post_form,thread=thread)
		post = Post(thread_id=thread.id,
					user_id=current_user.id,
					content=post_form.content.data)
		post_db.session.add(post)
		post_db.session.commit()
		return redirect(url_for("thread.showThread",thread_slug=thread_slug))

@post.route("/edit/<int:post_id>",methods=["GET","POST"])
@login_required
def editPost(post_id):
	post = Post.query.get_or_404(post_id)
	thread_slug = Thread.query.get_or_404(post.thread_id).slug
	if not post.user_id == current_user.id:
		abort(401)
	post_form = PostForm(request.form)
	if request.method == "POST":
		if not post_form.validate():
			return render_template("editPost.html",post_form=post_form,post=post)
		post.content = post_form.content.data
		post_db.session.commit()
		return redirect(url_for("thread.showThread",thread_slug=thread_slug))