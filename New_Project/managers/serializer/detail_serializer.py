from rest_framework import serializers

class ManagersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=150)
    description = serializers.CharField()
