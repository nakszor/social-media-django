from django.shortcuts import render, get_object_or_404
from rest_framework.generics import CreateAPIView, DestroyAPIView
from .models import Like
from .serializers import LikeSerializar
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from rest_framework.exceptions import ValidationError

class LikeView(CreateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()
    serializer_class = LikeSerializar
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        post = get_object_or_404(Post.objects.all(), id=self.kwargs["pk"])
        user = self.request.user
        already_exists = Like.objects.filter(post=post, user=user).first()
        if already_exists:
            raise ValidationError("message: voce ja deu like nesta publicaçao")
        return serializer.save(post=post, user=self.request.user)
    
    def get_object(self):
        user = self.request.user
        post = get_object_or_404(Post.objects.all(), id=self.kwargs["pk"])
        post_select = get_object_or_404(Like.objects.all(), post=post, user=user)
        return post_select