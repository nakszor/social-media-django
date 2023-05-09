from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Commentary
from .serializers import CommentarySerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from posts.models import Post
from posts.permissions import IsAccountOwner
from django.shortcuts import get_object_or_404
class CommentaryView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializers

    def paginate_queryset(self, queryset):
        return super().paginate_queryset(queryset)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        return serializer.save(post=post, user=self.request.user)
class CommentaryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Commentary.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAccountOwner]
    serializer_class = CommentarySerializers

    def perform_create(self, serializer):
        commentary = get_object_or_404(Commentary, pk=self.kwargs.get("pk"))
        return serializer.save(comment=commentary)
