from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .serializers import PostSerializers
from .permissions import IsAccountOwner


class PostView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)


class EditPostView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]

    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_url_kwarg = "post_id"
