from functools import reduce

from django.db.models import Q
from django.db import models


class ProductQuerySet(models.QuerySet):
    def search(self, query):
        try:
            fields = self.model.SEARCH_FIELDS
        except AttributeError:
            fields = []
        conditions = [Q(**{f"{field}__icontains": query}) for field in fields]
        if conditions:
            return self.filter(reduce(lambda x, y: x | y, conditions))
        return self.none()
