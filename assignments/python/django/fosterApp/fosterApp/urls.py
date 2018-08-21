"""fosterApp URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^users/', include('apps.users.urls', namespace="users")),
    url(r'^cats/', include('apps.cats.urls', namespace="cats")),
    #url(r'^dashboard/', include('apps.dashboard.urls', namespace="dashboard"))
]
