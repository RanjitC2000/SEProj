import graphene

import login.schema 


class Query(login.schema.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass

schema = graphene.Schema(query=Query)