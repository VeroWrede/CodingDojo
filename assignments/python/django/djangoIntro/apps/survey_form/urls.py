from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_survey', views.new_survey),
    url(r'^back', views.new_survey)
]
