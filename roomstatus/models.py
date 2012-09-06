from django.db import models

class DoorState(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	isOpen = models.BooleanField()

	def __unicode__(self):
		return "Door %s from %s to %s" % (
				"open" if self.isOpen else "closed",
				self.start.isoformat(),
				self.end.isoformat())

