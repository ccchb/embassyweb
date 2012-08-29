from django.shortcuts import render
from blog.models import Post

def index(request):
	posts = Post.objects.order_by('-updated')

	return render(request, "index.html", {"posts": posts})

