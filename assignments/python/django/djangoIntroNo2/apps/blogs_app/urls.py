from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<blog_num>\d+)/$', views.show),
    url(r'^(?P<blog_num>\d+)/edit/$', views.edit),
    url(r'^(?P<blog_num>\d+)/delete/$', views.delete),
]
