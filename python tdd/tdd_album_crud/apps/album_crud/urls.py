from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('album/create', views.create),
    path('album/<int:album_id>/edit', views.edit),
    path('album/delete', views.delete),
    path('album/<int:album_id>/read', views.read)
]
