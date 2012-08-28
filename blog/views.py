from models import Post
from django.shortcuts import render, get_object_or_404

def list_all(request):
	"""Lists all Posts"""
	posts = Post.objects.all()
	return render(request, "blog/list_all.html", {"posts": posts})

def show_all(request):
	"""Shows all Posts"""
	posts = Post.objects.all()
	return render(request, "blog/show_all.html", {"posts": posts})

def show_one(request, slug):
	"""Shows the Post with slug slug"""
	post = get_object_or_404(Post, slug=slug)
	return render(request, "blog/show_one.html", {"post": post})

