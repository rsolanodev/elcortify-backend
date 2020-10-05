from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText, FuzzyInteger, FuzzyDecimal

from elcortify.products.models import Product, Category


class CategoryFactory(DjangoModelFactory):
    name = FuzzyText()

    class Meta:
        model = Category


class ProductFactory(DjangoModelFactory):
    name = FuzzyText()
    price = FuzzyDecimal(0.99, 99.99)
    stock = FuzzyInteger(0, 200)
    category = SubFactory(CategoryFactory)

    class Meta:
        model = Product
