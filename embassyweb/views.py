from django.shortcuts import render
from blog.views import latest_public

def index(request):
	posts = latest_public()

	return render(request, "index.html", {"posts": posts})

