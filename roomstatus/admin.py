from django.contrib import admin
from models import *

class DoorStateAdmin(admin.ModelAdmin):
	list_display = ("isOpen", "start", "end")

class LeaseStateAdmin(admin.ModelAdmin):
	list_display = ("leases", "start", "end")

admin.site.register(DoorState, DoorStateAdmin)
admin.site.register(LeaseState, LeaseStateAdmin)

