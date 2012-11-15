from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from blog.views import PostsFeedRss, PostsFeedAtom

urlpatterns = patterns('',
	url(r'^$', 'embassyweb.views.index'),
	url(r'^favicon.ico$', 'embassyweb.views.favicon'),

	# blog
	url(r'^b/$', 'blog.views.list_all'),
	url(r'^b/all/$', 'blog.views.show_all'),
	url(r'^b/([a-zA-Z0-9_-]+)$', 'blog.views.show_one'),
	url(r'^b/feed.atom$', PostsFeedAtom(), name="feed-atom"),
	url(r'^b/feed.rss$', PostsFeedRss(), name="feed-rss"),

	# roomstatus
	url(r'^status.json$', 'roomstatus.views.spaceapi'),
	url(r'^status/door/set$', 'roomstatus.views.setDoorState'),

	# builtin django admin
	url(r'^admin/', include(admin.site.urls)),
)
