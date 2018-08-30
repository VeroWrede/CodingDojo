from django.conf.urls import url, include
from . import views 

urlpatterns = [
    url(r'^$', views.new, name='new'),
    url(r'create/$', views.create, name='create'),
    url(r'(?P<user_id>\d+)/show$', views.show, name='show')
]
