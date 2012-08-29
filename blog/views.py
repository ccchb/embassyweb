# -*- coding: utf-8 -*-

from models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed

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

class PostsFeedAtom(Feed):
	feed_type = Atom1Feed

	title = "Embassy of Nerdistan"
	subtitle = "Ein Ort für Nerds"
	link = "/"

	description_template = "blog/feed_item.html"

	def items(self):
		return Post.objects.all()

	def item_title(self, item):
		return item.title

	def item_pubdate(self, item):
		return item.updated

class PostsFeedRss(PostsFeedAtom):
	feed_type = Rss201rev2Feed
	description = PostsFeedAtom.subtitle

