from django.urls import path
from .views import IndexAPIView
from . import views

urlpatterns = [
    path("", IndexAPIView.as_view(), name="index"),
    path('add', views.add_num, name='add_num'),
    path('chat', views.chat, name='chat'),
]