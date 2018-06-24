from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^show_words', views.show_words),
	url(r'^add_word', views.add_word)

]