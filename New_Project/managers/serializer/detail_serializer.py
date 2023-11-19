from rest_framework import serializers
from ..models import Posts
from ..models import ModelSerializer


class ManagersSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return ModelSerializer(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class PostsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['name', 'description', 'comment']
