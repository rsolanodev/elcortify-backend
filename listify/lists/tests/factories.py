import factory
from django.utils import timezone
from factory.fuzzy import FuzzyText, FuzzyInteger

from listify.core.tests.factories import UserFactory
from listify.lists.models import Task, List


class TaskFactory(factory.django.DjangoModelFactory):
    text = FuzzyText()
    from_date = timezone.now()
    duration = FuzzyInteger(10, 120)

    class Meta:
        model = Task


class ListFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = List
