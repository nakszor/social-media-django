from rest_framework import serializers
from .models import Friend


class FriendsRetriever(serializers.ModelSerializer):
    username = serializers.CharField(source="friend.username")

    class Meta:
        model = Friend
        fields = ["id", "username", "created_at"]
