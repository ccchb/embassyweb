from django.db import models

class Post(models.Model):
	slug = models.SlugField(max_length=40, db_index=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('blog.views.show_one', [self.slug])

