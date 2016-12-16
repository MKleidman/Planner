from django.contrib import admin
from django.contrib.auth.models import User
from planner import models
import datetime

class UserAdmin(admin.ModelAdmin):
    pass


class PlannerListUserAdmin(admin.ModelAdmin):
    pass


class TasksInline(admin.TabularInline):
    model = models.Task


class PlannerListAdmin(admin.ModelAdmin):
    inlines = [TasksInline]


class SubTaskAdmin(admin.ModelAdmin):
    pass


class SubTasksInline(admin.TabularInline):
    model = models.SubTask


def complete_tasks(modeladmin, request, queryset):
    queryset.update(completed_at=datetime.datetime.now())
complete_tasks.short_description = "Mark Tasks as completed"


# class NonCompletedTaskListFilter(admin.SimpleListFilter):
#     title = 'Non Completed Tasks'
#     parameter_name = 'completed_at'

#     def queryset(self, request, queryset):
#         print "request", request
#         return queryset.filter(completed_at__isnull=True)


class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTasksInline]
    actions = [complete_tasks]

    def get_ordering(self, request):
        return ['completed_at']


admin.site.register(models.PlannerListUser, PlannerListUserAdmin)
admin.site.register(models.PlannerList, PlannerListAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.SubTask, SubTaskAdmin)
