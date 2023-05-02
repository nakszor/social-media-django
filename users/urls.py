from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("user/", views.UserView.as_view()),
    path("user/<int:user_id>/", views.UserViewId.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("refresh/", jwt_views.TokenRefreshView.as_view()),
]