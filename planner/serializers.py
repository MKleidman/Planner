from rest_framework import serializers
from planner import models

class PlannerListUserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.StringRelatedField()
    plannerlist = serializers.HyperlinkedRelatedField(view_name='plannerlist-detail', read_only=True)
    class Meta:
        model = models.PlannerListUser
        fields = ('user', 'plannerlist', 'type')


class SubTaskSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.HyperlinkedRelatedField(view_name='task-detail', read_only=True)
    class Meta:
        model = models.SubTask
        fields = ('task', 'created_date', 'updated_date', 'title', 'description', 'due_date', 'completed_at')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    plannerlist = serializers.HyperlinkedRelatedField(view_name='plannerlist-detail', read_only=True)
    subtask_set = SubTaskSerializer(many=True, read_only=True)
    users = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Task
        fields = ('plannerlist', 'priority', 'users', 'created_date', 'updated_date', 'title',
                  'description', 'due_date', 'completed_at', 'subtask_set')


class PlannerListSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.StringRelatedField(many=True)
    task_set = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = models.PlannerList
        fields = ('name', 'description', 'created_date', 'updated_date', 'start_date', 'end_date', 'users', 'task_set')
