from django.contrib import admin
from models import Attendant

class AttendantAdmin(admin.ModelAdmin):
    list_display = (
            "handle", "vegetarian", "needs_place_to_sleep", "email",
            "comments")

admin.site.register(Attendant, AttendantAdmin)

