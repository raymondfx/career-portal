import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from graphene import String
import django_filters
# convert TaggableManager to string representation
@convert_django_field.register(TaggableManager)
def convert_field_to_string(field, registry=None):
    return String(description=field.help_text, required=not field.null)


class StudentNode(DjangoObjectType):
    
    class Meta:
        model = Student
        filter_fields = ['username', 'password', 'confirm_password', 'student_id', 'first_name','middle_name','last_name','email','date_of_birth', 'gender', 'contact_number', 'resume']
        interfaces = (graphene.relay.Node,)
class StudentFilter(django_filters.FilterSet):
    # Do case-insensitive lookups on 'name'
    resume = django_filters.CharFilter(lookup_expr=['iexact'])

    class Meta:
        model = Student
        fields = ['username', 'password', 'confirm_password', 'student_id', 'first_name','middle_name','last_name','email','date_of_birth', 'gender', 'contact_number', 'resume']       

class EducationNode(DjangoObjectType):
    class Meta:
        model = Education
        filter_fields = ['course_type','course_name', 'major', 'institution_name', 'starting_date','completion_date']
        interfaces = (graphene.relay.Node,)
class ExperienceNode(DjangoObjectType):
    class Meta:
        model = Experience
        filter_fields = ['employer_name', 'job_title', 'is_current_job', 'start_date', 'end_date', 'job_description', 'location']
        interfaces = (graphene.relay.Node,)

class SkillNode(DjangoObjectType):
    class Meta:
        model = Skill
        filter_fields = ['skill_id', 'skill_name']
        interfaces = (graphene.relay.Node,)
class SkillFilter(django_filters.FilterSet):
    skill_name = django_filters.CharFilter(lookup_expr=['iexact'])

    class Meta:
        model = Skill
        fields = ['skill_id', 'skill_name']
class AppliedJobNode(DjangoObjectType):
    class Meta:
        model = AppliedJob
        filter_fields = ['student_id', 'employer_id', 'job_post_id']
        interfaces = (graphene.relay.Node,)
class Query(object):
    student = graphene.relay.Node.Field(StudentNode)
    all_students = DjangoFilterConnectionField(StudentNode, filterset_class=StudentFilter)

    education = graphene.relay.Node.Field(EducationNode)
    all_educations = DjangoFilterConnectionField(EducationNode)

    experience = graphene.relay.Node.Field(ExperienceNode)
    all_experience = DjangoFilterConnectionField(ExperienceNode)

    skill = graphene.relay.Node.Field(SkillNode)
    all_skills = DjangoFilterConnectionField(SkillNode, filterset_class=SkillFilter)

    appliedjob = graphene.relay.Node.Field(AppliedJobNode)
    all_appliedjobs = DjangoFilterConnectionField(AppliedJobNode)

