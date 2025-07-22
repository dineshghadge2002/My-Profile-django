from django.urls import path
from .views import IndexAPIView, AddAPIView, ChatAPIView
from . import views

urlpatterns = [
    path("", IndexAPIView.as_view(), name="index"),
    path('add', AddAPIView.as_view(), name='add_num'),
    path('chat', ChatAPIView.as_view(), name='chat'),
]