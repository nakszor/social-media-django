from rest_framework import serializers
from .models import Post, PrivacyOptions


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "privacy", "user_id", "created_at"]

    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=50)
    # content = serializers.CharField()
    # privacy = serializers.ChoiceField(choices=PrivacyOptions.choices)
    # created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
