from django.contrib import admin

# Register your models here.
from .models import *

class EmployerAdmin(admin.ModelAdmin):
    fields = ('employer_id', 'employer_name','description', 'email', 'phone', 'website', 'logo')

class StaffAdmin(admin.ModelAdmin):
    fields = ('staff_id', 'employer_id', 'first_name', 'last_name', 'job_title', 'phone_number', 'email', 'other_staff_details')

class JobTypeAdmin(admin.ModelAdmin):
    fields = ('job_id','job_type')

class JobPostAdmin(admin.ModelAdmin):
    fields = ('job_post_id', 'job_type', 'job_post_name', 'employer_id', 'created_date', 'job_description','job_requirement', 'job_location', 'is_active')


class JobPostActivityAdmin(admin.ModelAdmin):
    fields = ('activity_id', 'student_id', 'job_post_id', 'apply_date', 'job_application_status')

class JobLocationAdmin(admin.ModelAdmin):
    fields = ('location_id', 'street_address', 'city', 'county', 'country', 'zip_code')


class StudentInterviewAdmin(admin.ModelAdmin):
    fields = ('student_interview_id', 'student_id', 'employer_id', 'interview_datetime', 'student_interview_outcome', 'comment_by_employer', 'other_interview_details')

class Student_Interview_OutcomeAdmin(admin.ModelAdmin):
    fields = ('interview_outcome_id', 'student_id', 'interview_outcome')

class StudentPlacementAdmin(admin.ModelAdmin):
    fields = ('student_id', 'employer_id', 'placement_start_date', 'placement_manager_staffid', 'placement_end_date', 'comment_by_employer', 'comments_by_student', 'other_placement_details')

class StudentPlacementAssignmentAdmin(admin.ModelAdmin):
    fields = ('assignment_id', 'student_id', 'employer_id', 'assignment_start_date','assignment_end_date','supervisor', 'comments_by_supervisor', 'comments_by_student', 'other_assignment_details')



admin.site.register(Employer, EmployerAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(JobType, JobTypeAdmin)
admin.site.register(JobPost, JobPostAdmin)
admin.site.register(JobPostActivity, JobPostActivityAdmin)
admin.site.register(JobLocation, JobLocationAdmin)
admin.site.register(StudentInterview, StudentInterviewAdmin)
admin.site.register(Student_Interview_Outcome, Student_Interview_OutcomeAdmin)
admin.site.register(StudentPlacement, StudentPlacementAdmin)
admin.site.register(StudentPlacementAssignment, StudentPlacementAssignmentAdmin)