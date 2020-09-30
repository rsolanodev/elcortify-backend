from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class Task(TimeStampedModel):
    text = models.CharField(
        _("text"), max_length=250, help_text=_("Activity to be performed.")
    )
    from_date = models.DateTimeField(
        _("from date"), help_text=_("When the task should start.")
    )
    duration = models.IntegerField(
        _("duration"),
        help_text=_("Task duration in minutes."),
    )

    class Meta:
        verbose_name = _("task")
        verbose_name_plural = _("tasks")
        ordering = ("-created",)

    def __str__(self):
        return f"{self.from_date} to {self.to_date}"

    @property
    def to_date(self):
        """When the task should end."""
        return self.from_date + relativedelta(minutes=self.duration)


class List(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        help_text=_("List owner user."),
    )
    tasks = models.ManyToManyField(
        "lists.Task",
        related_name="lists",
        blank=True,
        verbose_name=_("tasks"),
    )

    class Meta:
        verbose_name = _("list")
        verbose_name_plural = _("lists")
        ordering = ("-created",)

    def __str__(self):
        return f"{self.user} list"
