from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/', views.new),
    url(r'^create/', views.create),
    url(r'^[0-9]{3}/edit/', views.edit),
    url(r'^[0-9]{3}/delete/', views.delete),
    url(r'^(?P<blog_num>\[0-9]{3})/', views.show)
]
