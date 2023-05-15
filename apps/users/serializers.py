from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)
