from django.db import models
from employer.models import *
from student.models import *
from phone_field import PhoneField

# Create your models here.
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.s_username, ext)
    return os.path.join('documents/', filename)

class Institution(models.Model):
    institution_id = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    location =  models.CharField(max_length=30)
    phone_number = PhoneField(max_length=30)
    logo = models.ImageField(upload_to=content_file_name, blank=True)

    def __str__(self):
        return self.institution_name

class Course(models.Model):
    course_id  = models.CharField(max_length=30)
    institution_id = models.ForeignKey(Institution, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=30)
    def __str__(self):
        return self.course_name

class Event(models.Model):
    event_id = models.CharField(max_length=30)
    event_title = models.CharField(max_length=30)
    event_description = models.CharField(max_length=200)
    event_date = models.DateField()
    event_start = models.DateField()
    event_end = models.DateField()
    organised_by = models.CharField(max_length=30)
    event_location = models.CharField(max_length=30)

    def __str__(self):
        return self.event_title

class EventAttendee(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = PhoneField(max_length=30)

    def __str__(self):
        return self.event_id

