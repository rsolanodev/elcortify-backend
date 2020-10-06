import django_filters

from elcortify.core.filters.filters import SearchFilter
from elcortify.products.models import Product


class ProductFilter(django_filters.FilterSet):
    category__id = ["exact"]
    ordering = django_filters.OrderingFilter(
        fields=[
            "name",
            "price",
            "created",
        ]
    )
    search = SearchFilter()

    class Meta:
        model = Product
        fields = ["category__id", "ordering", "search"]
