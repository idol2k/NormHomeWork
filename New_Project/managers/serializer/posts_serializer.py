from rest_framework import serializers
from ..models import Posts
from .comment_serializer import CommentSerializer

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=250)
    comment = CommentSerializer(many=True)

    def create(self, validated_data):
        return Posts.objects.create(**validated_data)