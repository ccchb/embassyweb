from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'embassyweb.views.index'),

	# builtin django admin
	url(r'^admin/', include(admin.site.urls)),
)
