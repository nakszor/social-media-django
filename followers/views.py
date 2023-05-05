from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import Follower
from .serializers import FollowerSerializer
from users.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from .permissions import IsFollowerToDelete


class followersDetailViewes(DestroyAPIView, CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsFollowerToDelete]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    lookup_url_kwarg = "pk"

    def get_object(self):
        user = self.request.user 
        pk = self.kwargs["pk"]
        get_object_or_404(self.queryset, followed_id=pk)
        res = get_object_or_404(self.queryset, followed=pk, follower=user)
        return res
    
    def perform_create(self, serializer):
        user = self.request.user
        arly_exists = Follower.objects.filter(followed=self.kwargs["pk"], follower=user).first()
        if arly_exists:
            raise ValidationError("message: voce ja segue esta pessoa")
        user_to_follow = get_object_or_404(User.objects.all(), id=self.kwargs["pk"])
        print("ola mundo")
        return serializer.save(followed=user_to_follow, follower=self.request.user)
    