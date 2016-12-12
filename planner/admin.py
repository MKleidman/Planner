from django.contrib import admin
from django.contrib.auth.models import User
from planner import models

class UserAdmin(admin.ModelAdmin):
    pass


class PlannerListUserAdmin(admin.ModelAdmin):
    pass


class PlannerListAdmin(admin.ModelAdmin):
    pass


class PlannerListAdmin(admin.ModelAdmin):
    pass


class SubTaskAdmin(admin.ModelAdmin):
    pass


class SubTasksInline(admin.TabularInline):
    model = models.SubTask

class TaskAdmin(admin.ModelAdmin):
    inlines = [SubTasksInline]
    pass


admin.site.register(models.PlannerListUser, PlannerListUserAdmin)
admin.site.register(models.PlannerList, PlannerListAdmin)
admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.SubTask, SubTaskAdmin)
