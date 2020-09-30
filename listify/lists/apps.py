from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ListsAppConfig(AppConfig):
    name = "listify.lists"
    verbose_name = _("Lists")
