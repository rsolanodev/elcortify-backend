from dateutil.relativedelta import relativedelta
from django.utils import timezone
from test_plus import TestCase

from listify.core.tests.factories import UserFactory
from listify.lists.models import Task
from listify.lists.tests.factories import ListFactory, TaskFactory


class ListTestCase(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user()

    def test_factories(self):
        basic_list = ListFactory(user=self.user)
        tasks = TaskFactory.create_batch(size=8)
        for task in tasks:
            basic_list.tasks.add(task)
        basic_list.save()
        self.assertEqual(len(tasks), Task.objects.all().count())

    def test_attr_to_date(self):
        from_date = timezone.now()
        task = TaskFactory(from_date=from_date, duration=120)
        self.assertEqual(from_date + relativedelta(hours=2), task.to_date)
