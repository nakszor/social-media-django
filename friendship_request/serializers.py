from rest_framework import serializers
from .models import Friendship
from friends.models import Friend


class FriendShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ["id", "user_id", "friend_id", "created_at"]
        read_only_fields = ["id", "user_id", "friend_id", "created_at"]
        deep = 1

    def create(self, validated_data):
        return Friendship.objects.create(**validated_data)


class FriendsShipRetriever(serializers.ModelSerializer):
    username = serializers.CharField(source="friend.username")
    friend_id = serializers.IntegerField(source="friend.id")

    class Meta:
        model = Friendship
        fields = ["id", "friend_id", "username", "created_at"]


class UpdateFriendshipStatusSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="friend.username", read_only=True)

    class Meta:
        model = Friendship
        fields = ["id", "username", "created_at"]
        read_only_fields = ["id", "username", "created_at"]

    def create(self, validated_data):
        friend_id = validated_data["friend"].id
        Friendship.objects.filter(friend_id=friend_id).delete()
        return Friend.objects.create(**validated_data)
