from django.contrib import admin

# Register your models here.
from .models import *

class InstitutionAdmin(admin.ModelAdmin):
    fields = ('institution_id', 'institution_name', 'address', 'email', 'location', 'phone_number', 'logo')

class  CourseAdmin(admin.ModelAdmin):
    fields = ('course_id', 'institution_name', 'course_name')

class EventAdmin(admin.ModelAdmin):
    fields = ('event_id', 'event_title', 'event_description', 'event_date', 'event_start', 'event_end', 'organised_by','event_location')

class EventAttendeeAdmin(admin.ModelAdmin):
    fields = ('event_id', 'first_name', 'last_name','email', 'phone_number')




admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventAttendee, EventAttendeeAdmin)
