from django.db import models
from institution.models import *
from employer.models import *
from phone_field import PhoneField
from taggit.managers import TaggableManager
from django.contrib.auth.models import AbstractUser
# Create your models here.
"""
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.s_username, ext)
    return os.path.join('documents/', filename)
"""

class Student(models.Model):
    GENDER=(
        ('F','Female'),
        ('M','Male'),
    )

    username = models.CharField(max_length=250, default='')
    password = models.CharField(max_length=250, blank=True)
    confirm_password=models.CharField(max_length=250, blank=True)
    student_id = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = email = models.EmailField(blank=False)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30, choices = GENDER, default='F')
    contact_number = PhoneField(max_length=100)
    resume = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.first_name 

class Education(models.Model):
    COURSE=(
        ('DIPLOMA','Diploma'),
        ('BACHELORS','Bachelors'),
        ('MASTERS','Masters'),
        ('PHD','Philospher'),
    )
    BRANCH=(
        ('CS','computer_science'),
        ('ME','mechanical'),
        ('EE','electrical'),
    )
    course_type = models.CharField(max_length=30,choices=COURSE, default='BACHELORS')
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    major = models.CharField(max_length=30)
    institution_name = models.CharField(max_length=30)
    starting_date = models.DateField()
    completion_date = models.DateField()

    def __str__(self):
        return self.course_name

class Experience(models.Model):
    employer_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    is_current_job = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    job_description = models.CharField(max_length=300)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.job_title

class Skill(models.Model):
    skill_id = models.CharField(max_length=30)
    skill_name = TaggableManager()

    def __str__(self):
        return self.skill_id

class AppliedJob(models.Model):
    student_id= models.CharField(max_length=30)
    employer_id = models.ForeignKey(Employer,on_delete=models.CASCADE)
    job_post_id = models.ForeignKey(JobPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_post_id

