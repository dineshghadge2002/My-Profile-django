from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('add', views.add_num, name='add_num'),
    path('chat', views.chat, name='chat'),
]