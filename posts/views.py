from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .serializers import PostSerializers
from .permissions import IsAccountOwner
from django.db.models import Q
from django.contrib.auth.models import AnonymousUser


class PostView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def get_queryset(self):

        myUser = self.request.user
        if isinstance(myUser, AnonymousUser):
            return Post.objects.filter(privacy="Public")
        myFriends = [friend.id for friend in myUser.friends.all()]
        return Post.objects.filter(Q(user_id__in=myFriends) | Q(privacy="Public"))

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
