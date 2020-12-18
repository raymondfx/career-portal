from django.contrib import admin

# Register your models here.
from .models import *

class StudentAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'confirm_password', 'student_id', 'first_name','middle_name','last_name','email','date_of_birth', 'gender', 'contact_number','resume')

class EducationAdmin(admin.ModelAdmin):
    fields = ('course_type','course_name', 'major', 'institution_name', 'starting_date','completion_date' )

class ExperienceAdmin(admin.ModelAdmin):
    fields = ('employer_name', 'job_title', 'is_current_job', 'start_date', 'end_date', 'job_description', 'location')

class SkillAdmin(admin.ModelAdmin):
    fields = ('skill_id','skill_name')


class AppliedJobAdmin(admin.ModelAdmin):
    fields = ('student_id', 'employer_id', 'job_post_id')

admin.site.register(Student, StudentAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(AppliedJob, AppliedJobAdmin)
