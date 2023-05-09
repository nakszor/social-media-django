from django.urls import path
from . import views

urlpatterns = [
    path("friendship/", views.FriendView.as_view()),
]
