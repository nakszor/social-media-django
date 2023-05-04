from django.urls import path
from . import views

urlpatterns = [
    path("comment/<int:pk>/", views.CommentaryView.as_view()),
    path("commentary/<int:pk>/", views.CommentaryDetailView.as_view()),
]
