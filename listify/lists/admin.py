from django.contrib import admin

from listify.lists.models import Task, List


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "from_date", "duration", "to_date", "created"]
    search_fields = ["text"]


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created"]
    search_fields = [
        "user__email",
        "user__username",
        "user__first_name",
        "user__last_name",
    ]
