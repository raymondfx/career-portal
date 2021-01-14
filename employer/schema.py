import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from graphene import String
import django_filters
from graphql_relay.node.node import from_global_id #for updating

@convert_django_field.register(TaggableManager)
def convert_field_to_string(field, registry=None):
    return String(description=field.help_text, required=not field.null)

class EmployerNode(DjangoObjectType):

    class Meta:
        model = Employer
        filter_fields = ['employer_id', 'employer_name','description', 'email', 'phone', 'website', 'logo']
        interfaces = (graphene.relay.Node,)

class EmployerFilter(django_filters.FilterSet):
    # Do case-insensitive lookups on 'name'
    logo = django_filters.CharFilter(lookup_expr=['iexact'])

    class Meta:
        model = Employer
        fields = ['employer_id', 'employer_name','description', 'email', 'phone', 'website', 'logo']

class StaffNode(DjangoObjectType):

    class Meta:
        model = Staff
        filter_fields = ['staff_id', 'employer_id', 'first_name', 'last_name', 'job_title', 'phone_number', 'email', 'other_staff_details']
        interfaces = (graphene.relay.Node,)

class JobTypeNode(DjangoObjectType):

    class Meta:
        model = JobType
        filter_fields = ['job_id','job_type']
        interfaces = (graphene.relay.Node,)

class JobPostNode(DjangoObjectType):

    class Meta:
        model = JobPost
        filter_fields = ['job_post_id', 'job_type', 'job_post_name', 'employer_id', 'created_date', 'job_description','job_requirement', 'job_location', 'is_active']
        interfaces = (graphene.relay.Node,)

class JobPostActivityNode(DjangoObjectType):

    class Meta:
        model = JobPostActivity
        filter_fields = ['activity_id', 'student_id', 'job_post_id', 'apply_date', 'job_application_status']
        interfaces = (graphene.relay.Node,)

class JobLocationNode(DjangoObjectType):

    class Meta:
        model = JobLocation
        filter_fields = ['location_id', 'street_address', 'city', 'county', 'country', 'zip_code']
        interfaces = (graphene.relay.Node,)

class StudentInterviewNode(DjangoObjectType):

    class Meta:
        model = StudentInterview
        filter_fields = ['student_interview_id', 'student_id', 'employer_id', 'interview_datetime', 'student_interview_outcome', 'comment_by_employer', 'other_interview_details']
        interfaces = (graphene.relay.Node,)

class Student_Interview_OutcomeNode(DjangoObjectType):

    class Meta:
        model = Student_Interview_Outcome
        filter_fields = ['interview_outcome_id', 'student_id', 'interview_outcome_description']
        interfaces = (graphene.relay.Node,)

class StudentPlacementNode(DjangoObjectType):

    class Meta:
        model = StudentPlacement
        filter_fields = ['student_id', 'employer_id', 'placement_start_date', 'placement_manager_staffid', 'placement_end_date', 'comment_by_employer', 'comments_by_student', 'other_placement_details']
        interfaces = (graphene.relay.Node,)

class StudentPlacementAssignmentNode(DjangoObjectType):

    class Meta:
        model = StudentPlacementAssignment
        filter_fields = ['assignment_id', 'student_id', 'employer_id', 'assignment_start_date','assignment_end_date','supervisor', 'comments_by_supervisor', 'comments_by_student', 'other_assignment_details']
        interfaces = (graphene.relay.Node,)


#Create Mutations
class CreateEmployer(graphene.relay.ClientIDMutation):
    employer = graphene.Field(EmployerNode)
    
    class Input:
        employer_id = graphene.String()
        employer_name = graphene.String()
        description = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        website = graphene.String()
        logo = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        employer = Employer(
            employer_id = input.get('employer_id'),
            employer_name = input.get('employer_name'),
            description = input.get('description'),
            email = input.get('email'),
            phone = input.get('phone'),
            website = input.get('website'),
            logo = input.get('logo')
        )
        employer.save()
    
        return CreateEmployer(employer=employer)

class CreateStaff(graphene.relay.ClientIDMutation):
    staff = graphene.Field(StaffNode)

    class Input:
        staff_id = graphene.String()
        employer_id = graphene.String() 
        first_name = graphene.String() 
        last_name = graphene.String() 
        job_title = graphene.String() 
        phone_number = graphene.String()
        email = graphene.String()
        other_staff_details = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        staff = Staff(
            staff_id = input.get('staff_id'),
            employer_id = input.get('staff_id'),
            first_name = input.get('first_name'),
            last_name = input.get('last_name'),
            job_title = input.get('job_title'),
            phone_number = input.get('phone_number'),
            email = input.get('email'),
            other_staff_details = input.get('other_staff_details')
        )
        staff.save()

        return CreateStaff(staff=staff)



class CreateJobType(graphene.relay.ClientIDMutation):
    jobtype = graphene.Field(JobTypeNode)

    class Input:
        job_id = graphene.String()
        job_type = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        jobtype = JobType(
            job_id = input.get('job_id'),
           job_type = input.get('job_type'),
        )
        jobtype.save()

        return CreateJobType(jobtype=jobtype)

class CreateJobPost(graphene.relay.ClientIDMutation):
    jobpost = graphene.Field(JobPostNode)

    class Input:
        job_post_id = graphene.String()
        job_type = graphene.String()
        job_post_name = graphene.String()
        employer_id = graphene.String()
        created_date = graphene.String() 
        job_description = graphene.String()
        job_requirement = graphene.String() 
        job_location = graphene.String()
        is_active = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        jobpost = JobPost(
            job_post_id = input.get('job_post_id'),
            job_type = input.get('job_type'),
            job_post_name = input.get('job_post_name'),
            employer_id = input.get('employer_id'),
            created_date = input.get('created_date'), 
            job_description = input.get('job_description'),
            job_requirement = input.get('job_requirement'),
            job_location = input.get('job_location'),
            is_active = input.get('is_active'),
        )
        jobpost.save()

        return CreateJobPost(jobpost=jobpost)

class CreateJobPostActivity(graphene.relay.ClientIDMutation):
    jobpostactivity = graphene.Field(JobTypeNode)

    class Input:
        activity_id = graphene.String()
        student_id = graphene.String()
        job_post_id = graphene.String() 
        apply_date = graphene.String()
        job_application_status = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        jobpostactivity = JobPostActivity(
            activity_id = input.get('activity_id'),
            student_id = input.get('student_id'),
            job_post_id = input.get('job_post_id'),
            apply_date = input.get('apply_date'),
            job_application_status = input.get('job_application_status'),
        )
        jobpostactivity.save()

        return CreateJobPostActivity(jobpostactivity=jobpostactivity)
    
#Update Class

class UpdateEmployer(graphene.relay.ClientIDMutation):
    employer = graphene.Field(EmployerNode)

    class Input:
        employer_id = graphene.String()
        employer_name = graphene.String()
        description = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        website = graphene.String()
        logo = graphene.String()

    def mutate_and_get_payload(root, info, **input):

        employer = Employer.objects.get(pk=from_global_id(input.get('id'))[1])
        employer.employer_name = input.get('employee_name')
        employer.description = input.get('description')
        employer.email = input.get('email')
        employer.phone = input.get('phone')
        employer.website =  input.get('website')
        employer.logo = input.get('logo')
        #employee.employee_city = City.objects.get(city_name=input.get(‘employee_city’))
        #employee.employee_title = Title.objects.get(title_name=input.get(‘employee_title’))
        employer.save()
        return UpdateEmployer(employer=employer)

class UpdateStaff(graphene.relay.ClientIDMutation):
    staff = graphene.Field(StaffNode)

    class Input:
        staff_id = graphene.String()
        employer_id = graphene.String() 
        first_name = graphene.String() 
        last_name = graphene.String() 
        job_title = graphene.String() 
        phone_number = graphene.String()
        email = graphene.String()
        other_staff_details = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        staff.staff_id = Staff.objects.get(pk=from_global_id(input.get('id'))[1])
        staff.employer_id = Employer.objects.get(employer_id=input.get('employer_id'))
        staff.first_name = input.get('first_name')
        staff.last_name = input.get('last_name')
        staff.job_title = input.get('job_title')
        staff.phone_number = input.get('phone_number')
        staff.save()
        return UpdateStaff(staff=staff)


class Query(object):
    employer = graphene.relay.Node.Field(EmployerNode)
    all_employers = DjangoFilterConnectionField(EmployerNode, filterset_class=EmployerFilter)

    staff = graphene.relay.Node.Field(StaffNode)
    all_staff = DjangoFilterConnectionField(StaffNode)

    jobtype = graphene.relay.Node.Field(JobTypeNode)
    all_jobtypes = DjangoFilterConnectionField(JobTypeNode)

    jobpost = graphene.relay.Node.Field(JobPostNode)
    all_jobposts = DjangoFilterConnectionField(JobPostNode)

    jobpostactivity = graphene.relay.Node.Field(JobPostActivityNode)
    all_jobpostactivities = DjangoFilterConnectionField(JobPostActivityNode)

    joblocation = graphene.relay.Node.Field(JobLocationNode)
    all_joblocations = DjangoFilterConnectionField(JobLocationNode)

    studentinterview = graphene.relay.Node.Field(StudentInterviewNode)
    all_studentinterviews = DjangoFilterConnectionField(StudentInterviewNode)

    studentinterviewoutcome = graphene.relay.Node.Field(Student_Interview_OutcomeNode)
    all_studentinterviewoutcomes = DjangoFilterConnectionField(Student_Interview_OutcomeNode)

    studentplacement = graphene.relay.Node.Field(StudentPlacementNode)
    all_studentplacements = DjangoFilterConnectionField(StudentPlacementNode)

    studentpalcementassignment = graphene.relay.Node.Field(StudentPlacementAssignmentNode)
    all_studentplacementassignments = DjangoFilterConnectionField(StudentPlacementAssignmentNode)

class Mutation(graphene.AbstractType):
    create_employer = CreateEmployer.Field()
    create_staff = CreateStaff.Field()
    create_jobtype = CreateJobType.Field()
    update_employer = UpdateEmployer.Field()
    update_staff = UpdateStaff.Field()