from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsAppConfig(AppConfig):
    name = "elcortify.products"
    verbose_name = _("Products")
