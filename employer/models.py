from django.db import models
from student.models import *
from phone_field import PhoneField
from taggit.managers import TaggableManager


# Create your models here.

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.s_username, ext)
    return os.path.join('documents/', filename)
    
class Employer(models.Model):
    employer_id = models.CharField(max_length=30)
    employer_name =  models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    phone = PhoneField(max_length=30)
    website = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.employer_name

class Staff(models.Model):
    staff_id = models.CharField(max_length=30)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    phone_number = PhoneField(max_length=30)
    email = models.CharField(max_length=30)
    other_staff_details = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class JobType(models.Model):
    job_id = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30)

    def __str__(self):
        return self.job_type

class JobPost(models.Model):
    job_post_id = models.CharField(max_length=30)
    job_type = models.ForeignKey(JobType, on_delete=models.CASCADE)
    job_post_name = models.CharField(max_length=30)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    created_date = models.DateField()
    job_description = models.CharField(max_length=200)
    job_requirement = models.CharField(max_length=200)
    skills = TaggableManager()
    job_location = models.CharField(max_length=30)
    is_active = models.CharField(max_length=30)

    def __str__(self):
        return self.job_post_name


class JobPostActivity(models.Model):
    activity_id = models.CharField(max_length=30)
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    job_post_id = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    apply_date = models.DateField()
    job_application_status = models.CharField(max_length=30)

    def __str__(self):
        return self.job_application_status

class JobLocation(models.Model):
    location_id = models.CharField(max_length=30)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)

    def __str__(self):
        return self.city


class StudentInterview(models.Model):
    student_interview_id = models.CharField(max_length=30)
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    student_interview_outcome = models.CharField(max_length=30)
    interview_datetime = models.DateField()
    comment_by_employer = models.CharField(max_length=30)
    other_interview_details = models.CharField(max_length=30)

    def __str__(self):
        return self.student_interview_id

class Student_Interview_Outcome(models.Model):
    OUTCOME =(
        ('P','Pending'),
        ('A','Accepted'),
        ('R', 'Rejected')
    )
    interview_outcome_id = models.CharField(max_length=30)
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    interview_outcome = models.CharField(max_length=30, choices = OUTCOME, default='P')

    def __str__(self):
        return self.interview_outcome_id

class StudentPlacement(models.Model):
    student_id = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    placement_start_date = models.DateField()
    placement_manager_staffid = models.CharField(max_length=30)
    placement_end_date = models.DateField()
    comment_by_employer = models.CharField(max_length=30)
    comments_by_student = models.CharField(max_length=30)
    other_placement_details = models.CharField(max_length=30)

    def __str__(self):
        return self.student_id

class StudentPlacementAssignment(models.Model):
    assignment_id = models.CharField(max_length=30)
    student_id = models.ForeignKey('student.Student',on_delete=models.CASCADE)
    employer_id = models.ForeignKey(Employer, on_delete=models.CASCADE)
    assignment_start_date = models.DateField()
    supervisor = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assignment_end_date = models.DateField()
    comments_by_supervisor = models.CharField(max_length=30)
    comments_by_student = models.CharField(max_length=30)
    other_assignment_details = models.CharField(max_length=30)
    
    def __str__(self):
        return self.student_placement_assignment_id