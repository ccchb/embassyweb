from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'embassyweb.views.index'),

	# blog
	url(r'^b/$', 'blog.views.list_all'),
	url(r'^b/all/$', 'blog.views.show_all'),
	url(r'^b/([a-zA-Z0-9_-]+)$', 'blog.views.show_one'),

	# builtin django admin
	url(r'^admin/', include(admin.site.urls)),
)
