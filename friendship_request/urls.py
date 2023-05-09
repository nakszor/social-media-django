from django.urls import path
from . import views

urlpatterns = [
    path("friendship/<int:pk>/", views.FriendShipView.as_view()),
    path("friendship/requests/", views.RetrieveFriendshipRequest.as_view()),
    path("friendship/requests/<int:pk>/", views.UpdateFriendshipStatusView.as_view()),
]
