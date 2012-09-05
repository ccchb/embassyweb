from django.db import models

class DoorState(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	state = models.BooleanField()

	def __unicode__(self):
		return "Door %s from %s to %s" % (
				"open" if self.state else "closed",
				self.start.isoformat(),
				self.end.isoformat())

