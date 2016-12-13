from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from planner import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register('plannerlistuser', views.PlannerListUserViewSet)
router.register('plannerlist', views.PlannerListViewSet)
router.register('task', views.TaskViewSet)
router.register('subtask', views.SubTaskViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
]
