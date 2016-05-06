from django.contrib import admin
from models import Attendant

class AttendantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attendant, AttendantAdmin)

