from django.urls import path
from . import views

urlpatterns = [
    path("follow/<int:pk>/", views.followersDetailViewes.as_view()),
]