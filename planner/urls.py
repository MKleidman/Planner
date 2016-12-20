from django.http import HttpResponse, HttpResponseForbidden
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import authenticate, login, models, logout
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import routers
from planner import views
from google_login.urls import urlpatterns as google_login_patterns

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

google_login_patterns += [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', health_check)
]
