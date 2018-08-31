from django.conf.urls import url, include
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create/', views.create, name='create'),
    url(r'new/', views.new, name='new'),
    url(r'(?P<user_id>\D+)/show$', views.show, name='show')
    #url(r'^(?P<user_id>\d+)/edit', views.edit, name="edit"),
]
