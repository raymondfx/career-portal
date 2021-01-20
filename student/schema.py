import graphene
from graphene_django import DjangoObjectType
from .models import *
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from graphene import String
import django_filters
from graphql_relay.node.node import from_global_id
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
#Create Schema Function
class CreateStudent(graphene.relay.ClientIDMutation):
    student = graphene.Field(StudentNode)

    class Input:
        username = graphene.String()
        password = graphene.String()
        confirm_password = graphene.String()
        student_id = graphene.String()
        first_name = graphene.String()
        middle_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        date_of_birth = graphene.String()
        gender = graphene.String()
        contact_number = graphene.String()
        resume = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        student = Student(
            username = input.get('username'),
            password = input.get('password'),
            confirm_password = input.get('confirm_password'),
            student_id = input.get('student_id'),
            first_name = input.get('first_name'),
            middle_name = input.get('middle_name'),
            last_name = input.get('last_name'),
            email = input.get('email'),
            date_of_birth = input.get('date_of_birth'),
            gender = input.get('gender'),
            contact_number = input.get('contact_number'),
            resume = input.get('resume'),
        )
        student.save()
        return CreateStudent(student=student)

class CreateEducation(graphene.relay.ClientIDMutation):
    eduaction = graphene.Field(EducationNode)

    class Input:
        course_type = graphene.String()
        course_name = graphene.String()
        major = graphene.String()
        institution_name = graphene.String()
        starting_date = graphene.String()
        completion_date = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        education = Education(
            course_type = input.get('course_type'),
            course_name = input.get('course_name'),
            major = input.get('major'),
            institution_name = input.get('institution_name'),
            starting_date = input.get('starting_date'),
            completion_date = input.get('completion_date'),
        )
        education.save()
        return CreateEducation(education=education)

class CreateExperience(graphene.relay.ClientIDMutation):
    experience = graphene.Field(ExperienceNode)

    class Input:
        employer_name = graphene.String()
        job_title = graphene.String()
        is_current_job = graphene.String()
        start_date = graphene.String()
        end_date = graphene.String()
        job_description = graphene.String()
        location = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        experience = Experience(
            employer_name = input.get('employer_name'),
            job_title = input.get('job_title'),
            is_current_job = input.get('is_current_job'),
            start_date = input.get('start_date'),
            end_date = input.get('end_date'),
            job_description = input.get('job_description'),
            location = input.get('location'),
        )
        experience.save()
        return CreateExperience(experience=experience)


class CreateSkill(graphene.relay.ClientIDMutation):
    skill = graphene.Field(SkillNode)

    class Input:
        skill_id = graphene.String()
        skill_name = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        skill = Skill(
          skill_id = input.get('skill_id'),
          skill_name = input.get('skill_name'),
        )
        skill.save()
        return CreateSkill(skill=skill)

class CreateAppliedJob(graphene.relay.ClientIDMutation):
    appliedjob = graphene.Field(AppliedJobNode)

    class Input:
        student_id = graphene.String()
        employer_id = graphene.String()
        job_post_id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        appliedjob = AppliedJob(
          student_id = input.get('student_id'),
          employer_id = input.get('employer_id'),
          job_post_id = input.get('job_post_id'),
        )
        appliedjob.save()
        return CreateAppliedJob(appliedjob=appliedjob)

#Update Schema Function

class UpdateStudent(graphene.relay.ClientIDMutation):
    student = graphene.Field(StudentNode)

    class Input:
        username = graphene.String()
        password = graphene.String()
        confirm_password = graphene.String()
        student_id = graphene.String()
        first_name = graphene.String()
        middle_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        date_of_birth = graphene.String()
        gender = graphene.String()
        contact_number = graphene.String()
        resume = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        student.username = input.get('username'),
        student.password = input.get('password'),
        student.confirm_password = input.get('confirm_password'),
        student.student_id = input.get('student_id'),
        student.first_name = input.get('first_name'),
        student.middle_name = input.get('middle_name'),
        student.last_name = input.get('last_name'),
        student.email = input.get('email'),
        student.date_of_birth = input.get('date_of_birth'),
        student.gender = input.get('gender'),
        student.contact_number = input.get('contact_number'),
        student.resume = input.get('resume'),
        student.save()
        return UpdateStudent(student=student)

class UpdateEducation(graphene.relay.ClientIDMutation):
    eduaction = graphene.Field(EducationNode)

    class Input:
        course_type = graphene.String()
        course_name = graphene.String()
        major = graphene.String()
        institution_name = graphene.String()
        starting_date = graphene.String()
        completion_date = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        eduaction.course_type = input.get('course_type'),
        eduaction.course_name = input.get('course_name'),
        eduaction.major = input.get('major'),
        eduaction.institution_name = input.get('institution_name'),
        eduaction.starting_date = input.get('starting_date'),
        eduaction.completion_date = input.get('completion_date'),
        education.save()
        return UpdateEducation(education=education)

class UpdateExperience(graphene.relay.ClientIDMutation):
    experience = graphene.Field(ExperienceNode)

    class Input:
        employer_name = graphene.String()
        job_title = graphene.String()
        is_current_job = graphene.String()
        start_date = graphene.String()
        end_date = graphene.String()
        job_description = graphene.String()
        location = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        experience.employer_name = input.get('employer_name'),
        experience.job_title = input.get('job_title'),
        experience.is_current_job = input.get('is_current_job'),
        experience.start_date = input.get('start_date'),
        experience.end_date = input.get('end_date'),
        experience.job_description = input.get('job_description'),
        experience.location = input.get('location'),
        experience.save()
        return UpdateExperience(experience=experience)


class UpdateSkill(graphene.relay.ClientIDMutation):
    skill = graphene.Field(SkillNode)

    class Input:
        skill_id = graphene.String()
        skill_name = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        skill.skill_id = input.get('skill_id'),
        skill.skill_name = input.get('skill_name'),
        skill.save()
        return UpdateSkill(skill=skill)

class UpdateAppliedJob(graphene.relay.ClientIDMutation):
    appliedjob = graphene.Field(AppliedJobNode)

    class Input:
        student_id = graphene.String()
        employer_id = graphene.String()
        job_post_id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        appliedjob.student_id = input.get('student_id'),
        appliedjob.employer_id = input.get('employer_id'),
        appliedjob.job_post_id = input.get('job_post_id'),
        appliedjob.save()
        return UpdateAppliedJob(appliedjob=appliedjob)

# Delete Schema Function
class DeleteStudent(graphene.relay.ClientIDMutation):
    student = graphene.Field(StudentNode)

    class Input:
        username = graphene.String()
        password = graphene.String()
        confirm_password = graphene.String()
        student_id = graphene.String()
        first_name = graphene.String()
        middle_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        date_of_birth = graphene.String()
        gender = graphene.String()
        contact_number = graphene.String()
        resume = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        username = input.get('username'),
        password = input.get('password'),
        confirm_password = input.get('confirm_password'),
        student_id = input.get('student_id'),
        first_name = input.get('first_name'),
        middle_name = input.get('middle_name'),
        last_name = input.get('last_name'),
        email = input.get('email'),
        date_of_birth = input.get('date_of_birth'),
        gender = input.get('gender'),
        contact_number = input.get('contact_number'),
        resume = input.get('resume'),
        student.delete()
        return DeleteStudent(student=student)

class DeleteEducation(graphene.relay.ClientIDMutation):
    eduaction = graphene.Field(EducationNode)

    class Input:
        course_type = graphene.String()
        course_name = graphene.String()
        major = graphene.String()
        institution_name = graphene.String()
        starting_date = graphene.String()
        completion_date = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        course_type = input.get('course_type'),
        course_name = input.get('course_name'),
        major = input.get('major'),
        institution_name = input.get('institution_name'),
        starting_date = input.get('starting_date'),
        completion_date = input.get('completion_date'),
        education.delete()
        return DeleteEducation(education=education)

class DeleteExperience(graphene.relay.ClientIDMutation):
    experience = graphene.Field(ExperienceNode)

    class Input:
        employer_name = graphene.String()
        job_title = graphene.String()
        is_current_job = graphene.String()
        start_date = graphene.String()
        end_date = graphene.String()
        job_description = graphene.String()
        location = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        employer_name = input.get('employer_name'),
        job_title = input.get('job_title'),
        is_current_job = input.get('is_current_job'),
        start_date = input.get('start_date'),
        end_date = input.get('end_date'),
        job_description = input.get('job_description'),
        location = input.get('location'),
        experience.delete()
        return DeleteExperience(experience=experience)


class DeleteSkill(graphene.relay.ClientIDMutation):
    skill = graphene.Field(SkillNode)

    class Input:
        skill_id = graphene.String()
        skill_name = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        skill_id = input.get('skill_id'),
        skill_name = input.get('skill_name'),
        skill.delete()
        return DeleteSkill(skill=skill)

class DeleteAppliedJob(graphene.relay.ClientIDMutation):
    appliedjob = graphene.Field(AppliedJobNode)

    class Input:
        student_id = graphene.String()
        employer_id = graphene.String()
        job_post_id = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        student_id = input.get('student_id'),
        employer_id = input.get('employer_id'),
        job_post_id = input.get('job_post_id'),
        appliedjob.delete()
        return DeleteAppliedJob(appliedjob=appliedjob)
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



class Mutation(graphene.AbstractType):
    create_student = CreateStudent.Field()
    create_education = CreateEducation.Field()
    create_experience = CreateExperience.Field()
    create_skill = CreateSkill.Field()
    create_appliedjob = CreateAppliedJob.Field()

    update_student = UpdateStudent.Field()
    update_education = UpdateEducation.Field()
    update_experience = UpdateExperience.Field()
    update_skill = UpdateSkill.Field()
    update_appliedjob = UpdateAppliedJob.Field()

    delete_student = DeleteStudent.Field()
    delete_education = DeleteEducation.Field()
    delete_experience = DeleteExperience.Field()
    delete_skill = DeleteSkill.Field()
    delete_appliedjob = DeleteAppliedJob.Field()