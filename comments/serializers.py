from rest_framework import serializers
from .models import Commentary


class CommentarySerializers(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ["id", "content", "user_id","post_id","created_at"]
