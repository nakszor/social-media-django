from django.urls import path
from . import views

urlpatterns = [
    path("like/<int:pk>/", views.LikeView.as_view()),
]