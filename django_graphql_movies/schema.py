import graphene
import movies.schema


class Query(movies.schema.Query, graphene.ObjectType):
	pass


class Mutation(movies.schema.Mutation, graphene.ObjectType):
	pass


graphene.Schema(query=Query, mutation=Mutation)
