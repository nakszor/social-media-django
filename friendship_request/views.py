from .models import Friendship
from .serializers import (
    FriendShipSerializer,
    FriendsShipRetriever,
    UpdateFriendshipStatusSerializer,
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from django.shortcuts import get_object_or_404
from users.models import User


class FriendShipView(CreateAPIView, DestroyAPIView):
    queryset = Friendship.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FriendShipSerializer

    def perform_create(self, serializer):
        userFriendshipRequest = get_object_or_404(User, pk=self.kwargs.get("pk"))
        return serializer.save(friend=userFriendshipRequest, user=self.request.user)


class RetrieveFriendshipRequest(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FriendsShipRetriever

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(user=user)


class UpdateFriendshipStatusView(CreateAPIView, DestroyAPIView):
    queryset = Friendship.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateFriendshipStatusSerializer

    def perform_create(self, serializer):
        friendship = get_object_or_404(User, pk=self.kwargs.get("pk"))
        return serializer.save(friend=friendship)
