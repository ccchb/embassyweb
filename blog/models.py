# -*- coding: utf-8 -*-

from django.db import models
import re

slug_length = 40

def leetsluggify(text):
	"""The greatest sluggifier on this planet"""
	
	# dirty hack to transliterate german umlauts
	ger_repl = {
		u"ä":u"ae",
		u"ö":u"oe",
		u"ü":u"ue",
		u"Ä":u"Ae",
		u"Ö":u"Oe",
		u"Ü":u"Ue",
		u"ß":u"ss",
	}
	for a, b in ger_repl.items():
		text = text.replace(a, b)
	
	# delete everything except slug-chars and space
	text = re.sub(ur"[^ a-zA-Z0-9_-]+", "", text)
	
	# convert to camelCase
	def repl(s):
		s = s.group(0).strip()
		return s.upper()
	text = re.sub(ur" +[^ ]", repl, text)
	text = text.strip()
	
	# if the text is too long, remove every "e" (~17% of all chars)
	if len(text) > slug_length:
		text = text.replace(u"e", u"")
	
	# finally, select the first $slug_length characters
	text = text[:slug_length]
	
	return text

class Post(models.Model):
	slug = models.SlugField(max_length=slug_length, unique=True,
			db_index=True, editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	public = models.BooleanField(default=True)
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __unicode__(self):
		if self.public:
			return "%s" % (self.title)
		else:
			return "(hidden) %s" % (self.title)

	@models.permalink
	def get_absolute_url(self):
		return ('blog.views.show_one', [self.slug])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = leetsluggify(self.title)
		
		super(Post, self).save(*args, **kwargs)
