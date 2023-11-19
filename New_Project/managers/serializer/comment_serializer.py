from rest_framework import serializers
from ..models import Comment

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name_comment = serializers.CharField(max_length=50)
    text_comment = serializers.CharField(max_length=150)
    category = serializers.CharField(max_length=20)

    def create(self, validate_data):
        return Comment.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name_comment = validated_data.get('name_comment', instance.name_comment)
        instance.text_comment = validated_data.get('text_comment', instance.text_comment)
        instance.save()
        return instance