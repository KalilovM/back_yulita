from rest_framework import serializers

from .models import Cloth


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = '__all__'


class ClothListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = (
            'id',
            'name',
            'article',
            'suit',
        )
        