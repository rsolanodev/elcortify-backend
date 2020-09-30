import graphene
from graphene_django import DjangoObjectType

from listify.lists.models import Task, List


class TaskType(DjangoObjectType):
    to_date = graphene.String(source='to_date')

    class Meta:
        model = Task
        fields = ["id", "text", "from_date", "duration", "to_date", "created"]


class ListType(DjangoObjectType):
    class Meta:
        model = List
        fields = ["id", "user", "tasks", "created"]


class Query(graphene.ObjectType):
    lists_by_username = graphene.List(ListType, username=graphene.String(required=True))

    def resolve_lists_by_username(root, info, username):
        return List.objects.filter(user__username=username)


schema = graphene.Schema(query=Query)
