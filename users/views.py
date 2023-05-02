from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import User
from .serializer import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import CreateOrIsAcontOner


class UserView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateOrIsAcontOner]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewId(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [CreateOrIsAcontOner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"
    