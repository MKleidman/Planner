from django.http import HttpResponse, HttpResponseForbidden
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import authenticate, login, models, logout
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import routers
from planner import views
from oauth2client import client, crypt

def complete_login(request):
    try:
        idinfo = client.verify_id_token(request.POST['idtoken'], settings.GOOGLE_CLIENT_ID)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")

        # If auth request is from a G Suite domain:
        #if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #    raise crypt.AppIdentityError("Wrong hosted domain.")
    except crypt.AppIdentityError:
        # Invalid token
        return HttpResponseForbidden()
    userid = idinfo['sub']
    user = models.User.objects.get(email=request.POST['email'])
    login(request, user)
    return HttpResponse('<html><body>{}</body></html>'.format(user.id), content_type='text/html')

@ensure_csrf_cookie
def login_view(request):
    return render_to_response('google-login.html',
                              {"next": request.GET.get('next'), "google_client_id": settings.GOOGLE_CLIENT_ID})

def logout_view(request):
    logout(request)
    return render_to_response('google-logout.html', content_type='text/html')

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
    url(r'^admin/login/', login_view),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login_view),
    url(r'^complete_login/$', complete_login),
    url(r'^admin/logout/', logout_view),
    url(r'', health_check)
]
