from django.db import models


class PlannerListUser(models.Model):
    USER_TYPES = [
        ('creator', 'Creator'),
        ('manager', 'Manager'),
        ('watcher', 'Watcher')
    ]
    user = models.ForeignKey('auth.User')
    plannerlist = models.ForeignKey('planner.PlannerList')
    type = models.CharField(db_index=True, max_length=20, choices=USER_TYPES)

    def __unicode__(self):
        return "{} ({})".format(self.user.username, self.type)


class PlannerList(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)
    start_date = models.DateTimeField(db_index=True, null=True, blank=True)
    end_date = models.DateTimeField(db_index=True, null=True, blank=True)
    users = models.ManyToManyField('auth.User', through=PlannerListUser)

    def __unicode__(self):
        return "List: {}".format(self.name)


class Task(models.Model):
    PRIORITIES = [
        (1, 'Wish List'),
        (2, 'Low'),
        (3, 'Medium'),
        (4, 'High'),
        (5, 'Critical')
    ]
    plannerlist = models.ForeignKey('planner.PlannerList')
    priority = models.IntegerField(db_index=True, choices=PRIORITIES)
    users = models.ManyToManyField('auth.User')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __unicode__(self):
        return self.title


class SubTask(models.Model):
    task = models.ForeignKey('planner.Task')
    created_date = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_date = models.DateTimeField(auto_now=True, db_index=True)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True, db_index=True)
    completed_at = models.DateTimeField(null=True, blank=True, db_index=True)

    def __unicode__(self):
        return self.title
