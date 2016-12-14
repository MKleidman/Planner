from rest_framework import viewsets
from planner import models, serializers

class PlannerListUserViewSet(viewsets.ModelViewSet):
    queryset = models.PlannerListUser.objects.all()
    serializer_class = serializers.PlannerListUserSerializer


class PlannerListViewSet(viewsets.ModelViewSet):
    queryset = models.PlannerList.objects.all()
    serializer_class = serializers.PlannerListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer


class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = models.SubTask.objects.all()
    serializer_class = serializers.SubTaskSerializer
