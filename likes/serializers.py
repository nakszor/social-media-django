from rest_framework import serializers
from .models import Like
from users.serializer import UserSerializer
from posts.serializers import PostSerializers


class LikeSerializar(serializers.ModelSerializer):
    user_id = UserSerializer
    post_id = PostSerializers

    class Meta:
        model = Like
        fields = ["id", "user", "post", "created_at"]
        read_only_fields = ["id", "user", "post", "created_at"]
        deep = 1

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

