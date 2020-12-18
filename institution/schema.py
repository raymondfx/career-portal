import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from graphene import String
import django_filters

@convert_django_field.register(TaggableManager)
def convert_field_to_string(field, registry=None):
    return String(description=field.help_text, required=not field.null)

class InstitutionNode(DjangoObjectType):

    class Meta:
        model = Institution
        filter_fields = ['institution_id', 'institution_name', 'address', 'email', 'location', 'phone_number', 'logo']
        interfaces = (graphene.relay.Node,)
class InstitutionFilter(django_filters.FilterSet):
    # Do case-insensitive lookups on 'name'
    logo = django_filters.CharFilter(lookup_expr=['iexact'])

    class Meta:
        model = Institution
        fields = ['institution_id', 'institution_name', 'address', 'email', 'location', 'phone_number', 'logo']

class CourseNode(DjangoObjectType):

    class Meta:
        model = Course
        filter_fields = ['course_id', 'institution_id', 'course_name']
        interfaces = (graphene.relay.Node,)

class EventNode(DjangoObjectType):

    class Meta:
        model = Event
        filter_fields = ['event_id', 'event_title', 'event_description', 'event_date', 'event_start', 'event_end', 'organised_by','event_location']
        interfaces = (graphene.relay.Node,)

class StudentEventAttendeeNode(DjangoObjectType):

    class Meta:
        model = StudentEventAttendee
        filter_fields = ['student_id', 'event_id', 'first_name', 'last_name','email', 'phone_number']
        interfaces = (graphene.relay.Node,)

class EmployerEventAttendeeNode(DjangoObjectType):

    class Meta:
        model = EmployerEventAttendee
        filter_fields = ['employer_id', 'employer_name', 'email', 'phone_number']
        interfaces = (graphene.relay.Node,)

class Query(object):
    institution = graphene.relay.Node.Field(InstitutionNode)
    all_institutions = DjangoFilterConnectionField(InstitutionNode, filterset_class=InstitutionFilter)

    course = graphene.relay.Node.Field(CourseNode)
    all_courses = DjangoFilterConnectionField(CourseNode)

    event = graphene.relay.Node.Field(EventNode)
    all_events = DjangoFilterConnectionField(EventNode)

    studenteventattendee = graphene.relay.Node.Field(StudentEventAttendeeNode)
    all_studenteventattendees = DjangoFilterConnectionField(StudentEventAttendeeNode)

    employerEeventattendee = graphene.relay.Node.Field(EmployerEventAttendeeNode)
    all_employerEeventattendees = DjangoFilterConnectionField(EmployerEventAttendeeNode)