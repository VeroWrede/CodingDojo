from django.conf.urls import url
import views

urlpatters = [
	url(r'^$', views.index)
]