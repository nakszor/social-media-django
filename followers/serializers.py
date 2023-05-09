from rest_framework import serializers
from .models import Follower
from users.serializer import UserSerializer 


class FollowerSerializer(serializers.ModelSerializer):

    followed = UserSerializer
    follower = UserSerializer

    class Meta:
        model = Follower
        fields = ["id", "followed", "follower", "created_at"]
        read_only_fields = ["id", "followed", "follower", "created_at"]
        deep = 1

    def create(self, validated_data):
        return Follower.objects.create(**validated_data)
        


