import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from graphene import String
import django_filters
from graphql_relay.node.node import from_global_id

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

class EventAttendeeNode(DjangoObjectType):

    class Meta:
        model = EventAttendee
        filter_fields = ['event_id', 'first_name', 'last_name','email', 'phone_number']
        interfaces = (graphene.relay.Node,)


#Create Schema Function

class CreateInsitution(graphene.relay.ClientIDMutation):
    institution = graphene.Field(InstitutionNode)

    class Input:
        institution_id = graphene.String()
        institution_name = graphene.String()
        address = graphene.String()
        email = graphene.String()
        location = graphene.String()
        phone_number = graphene.String()
        logo = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        institution = Institution(
            institution_id = input.get('institution_id'),
            institution_name = input.get('institution_name'),
            address = input.get('address'),
            email = input.get('email'),
            location = input.get('location'),
            phone_number = input.get('phone_number'),
            logo = input.get('logo'),
        )
        institutio.save()
        return CreateInsitution(institution=institution)
class CreateCourse(graphene.relay.ClientIDMutation):
    course = graphene.Field(CourseNode)

    class Input:
        course_id = graphene.String()
        institution_id = graphene.String()
        course_name = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        course = Course(
            course_id = input.get('course_id'),
            institution_id = input.get('institution_id'),
            course_name = input.get('course_name'),
        )
        course.save()
        return CreateCourse(course=course)
class CreateEvent(graphene.relay.ClientIDMutation):
    event = graphene.Field(EventNode)

    class Input:
        event_id = graphene.String()
        event_title = graphene.String()
        event_description = graphene.String()
        event_date = graphene.String()
        event_start = graphene.String()
        event_end = graphene.String()
        organised_by = graphene.String()
        event_location = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        event = Event(
            event_id = input.get('event_id'),
            event_title = input.get('event_title'),
            event_description = input.get('event_description'),
            event_date = input.get('event_date'),
            event_start = input.get('event_start'),
            event_end = input.get('event_end'),
            organised_by = input.get('organised_by'),
            event_location = input.get('event_location'),
        )
        event.save()
        return CreateEvent(event=event)

class CreateEventAttendee(graphene.relay.ClientIDMutation):
    eventattendee = graphene.Field(EventAttendeeNode)

    class Input:
        event_id = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone_number = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        event = EventAttendee(
           event_id = input.get('event_id'),
           first_name = input.get('first_name'),
           last_name = input.get('last_name'),
           email = input.get('email'),
           phone_number = input.get('phone_number'),
        )
        eventattendee.save()
        return CreateEventAttendee(eventattendee=eventattendee)
#Update Schema Function

class UpdateInsitution(graphene.relay.ClientIDMutation):
    institution = graphene.Field(InstitutionNode)

    class Input:
        institution_id = graphene.String()
        institution_name = graphene.String()
        address = graphene.String()
        email = graphene.String()
        location = graphene.String()
        phone_number = graphene.String()
        logo = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        institution.institution_id = input.get('institution_id')
        institution.institution_name = input.get('institution_name')
        institution.address = input.get('address')
        institution.email = input.get('email')
        institution.location = input.get('location')
        institution.phone_number = input.get('phone_number')
        institution.logo = input.get('logo')
        institutio.save()
        return UpdateInsitution(institution=institution)
class UpdateCourse(graphene.relay.ClientIDMutation):
    course = graphene.Field(CourseNode)

    class Input:
        course_id = graphene.String()
        institution_id = graphene.String()
        course_name = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        course.course_id = input.get('course_id')
        course.institution_id = input.get('institution_id')
        course.course_name = input.get('course_name')
        course.save()
        return UpdateCourse(course=course)
class UpdateEvent(graphene.relay.ClientIDMutation):
    event = graphene.Field(EventNode)

    class Input:
        event_id = graphene.String()
        event_title = graphene.String()
        event_description = graphene.String()
        event_date = graphene.String()
        event_start = graphene.String()
        event_end = graphene.String()
        organised_by = graphene.String()
        event_location = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        event.event_id = input.get('event_id')
        event.event_title = input.get('event_title')
        event.event_description = input.get('event_description')
        event.event_date = input.get('event_date')
        event.event_start = input.get('event_start')
        event.event_end = input.get('event_end')
        event.organised_by = input.get('organised_by')
        event.event_location = input.get('event_location')
        event.save()
        return UpdateEvent(event=event)

class UpdateEventAttendee(graphene.relay.ClientIDMutation):
    eventattendee = graphene.Field(EventAttendeeNode)

    class Input:
        event_id = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone_number = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        eventattendee.event_id = input.get('event_id')
        eventattendee.first_name = input.get('first_name')
        eventattendee.last_name = input.get('last_name')
        eventattendee.email = input.get('email')
        eventattendee.phone_number = input.get('phone_number')
        eventattendee.save()
        return UpdateEventAttendee(eventattendee=eventattendee)
#Delete Function

class DeleteInsitution(graphene.relay.ClientIDMutation):
    institution = graphene.Field(InstitutionNode)

    class Input:
        institution_id = graphene.String()
        institution_name = graphene.String()
        address = graphene.String()
        email = graphene.String()
        location = graphene.String()
        phone_number = graphene.String()
        logo = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        nstitution_id = input.get('institution_id')
        institution_name = input.get('institution_name')
        address = input.get('address')
        email = input.get('email')
        location = input.get('location')
        phone_number = input.get('phone_number')
        logo = input.get('logo')
        institutio.delete()
        return DeleteInsitution(institution=institution)
class DeleteCourse(graphene.relay.ClientIDMutation):
    course = graphene.Field(CourseNode)

    class Input:
        course_id = graphene.String()
        institution_id = graphene.String()
        course_name = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        course_id = input.get('course_id')
        institution_id = input.get('institution_id')
        course_name = input.get('course_name')
        course.delete()
        return DeleteCourse(course=course)
class DeleteEvent(graphene.relay.ClientIDMutation):
    event = graphene.Field(EventNode)

    class Input:
        event_id = graphene.String()
        event_title = graphene.String()
        event_description = graphene.String()
        event_date = graphene.String()
        event_start = graphene.String()
        event_end = graphene.String()
        organised_by = graphene.String()
        event_location = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        event_id = input.get('event_id')
        event_title = input.get('event_title')
        event_description = input.get('event_description')
        event_date = input.get('event_date')
        event_start = input.get('event_start')
        event_end = input.get('event_end')
        organised_by = input.get('organised_by')
        event_location = input.get('event_location')
        event.delete()
        return DeleteEvent(event=event)

class DeleteEventAttendee(graphene.relay.ClientIDMutation):
    eventattendee = graphene.Field(EventAttendeeNode)

    class Input:
        event_id = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone_number = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        event_id = input.get('event_id')
        first_name = input.get('first_name')
        last_name = input.get('last_name')
        email = input.get('email')
        phone_number = input.get('phone_number')
        eventattendee.delete()
        return DeleteEventAttendee(eventattendee=eventattendee)
class Query(object):
    institution = graphene.relay.Node.Field(InstitutionNode)
    all_institutions = DjangoFilterConnectionField(InstitutionNode, filterset_class=InstitutionFilter)

    course = graphene.relay.Node.Field(CourseNode)
    all_courses = DjangoFilterConnectionField(CourseNode)

    event = graphene.relay.Node.Field(EventNode)
    all_events = DjangoFilterConnectionField(EventNode)

    eventattendee = graphene.relay.Node.Field(EventAttendeeNode)
    all_eventattendees = DjangoFilterConnectionField(EventAttendeeNode)

class Mutation(graphene.AbstractType):
    create_institution = CreateInsitution.Field()
    create_course = CreateCourse.Field()
    create_event = CreateEvent.Field()
    create_eventattendee = CreateEventAttendee.Field()

    update_institution = UpdateInsitution.Field()
    update_course = UpdateCourse.Field()
    update_event = UpdateEvent.Field()
    update_eventattendee = UpdateEventAttendee.Field()

    delete_institution = DeleteInsitution.Field()
    delete_course = DeleteCourse.Field()
    delete_event = DeleteEvent.Field()
    delete_eventattendee = DeleteEventAttendee.Field()