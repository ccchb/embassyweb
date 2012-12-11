from django.db import models

class DoorState(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	isOpen = models.BooleanField()

class LeaseState(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()
	leases = models.IntegerField()


