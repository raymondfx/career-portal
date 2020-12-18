import graphene
import student.schema
import employer.schema
import institution.schema


class Query(student.schema.Query,employer.schema.Query, institution.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)