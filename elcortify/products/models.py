from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

from elcortify.products.managers import ProductQuerySet


class Category(TimeStampedModel):
    name = models.CharField(_("name"), max_length=200, unique=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ("name",)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(_("name"), max_length=250)
    price = models.DecimalField(
        _("price"),
        max_digits=20,
        decimal_places=2,
    )
    stock = models.IntegerField(_("stock"))
    category = models.ForeignKey(
        "products.Category",
        verbose_name=_("category"),
        related_name="products",
        on_delete=models.PROTECT,
    )

    objects = ProductQuerySet.as_manager()

    SEARCH_FIELDS = [
        "name",
        "category__name",
    ]

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        ordering = ("-created",)

    def __str__(self):
        return self.name
