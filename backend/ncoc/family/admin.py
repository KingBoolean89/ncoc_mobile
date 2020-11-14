from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_time', 'end_time')


class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob')


admin.site.register(Event, EventAdmin)
admin.site.register(Child, ChildAdmin)
