from django.http import HttpResponse
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from rest_framework import routers
from planner import views

def login_view(request):
	return render_to_response('google-login.html')

def health_check(request):
    """Health check for determining if the server is available in an Amazon Elastic Load Balancer."""
    response_content = '<html><body>OK</body></html>'
    return HttpResponse(response_content, content_type='text/html')

admin.autodiscover()

router = routers.DefaultRouter()
router.register('plannerlistuser', views.PlannerListUserViewSet)
router.register('plannerlist', views.PlannerListViewSet)
router.register('task', views.TaskViewSet)
router.register('subtask', views.SubTaskViewSet)

urlpatterns = [
	url(r'^api/v1/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^login/$', login_view),
	url(r'^/$', health_check)
]
