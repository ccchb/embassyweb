from django.contrib import admin
from models import Attendant

class AttendantAdmin(admin.ModelAdmin):
    exclude = ()

admin.site.register(Attendant, AttendantAdmin)

