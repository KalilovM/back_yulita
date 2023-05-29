from rest_framework import serializers

from .models import Cloth, ClothType, Suit


class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = '__all__'


class ClothListSerializer(serializers.ModelSerializer):
    preview_image = serializers.SerializerMethodField()
    class Meta:
        model = Cloth
        fields = (
            'id',
            'name',
            'article',
            'suit',
            'preview_image'
        )
        
    def get_preview_image(self, obj):
        request = self.context.get('request')
        image = obj.model_images.first()
        if image:
            return request.build_absolute_uri(image.image.url)
    
       
class ClothTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothType
        fields = '__all__'
        
class SuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suit
        fields = '__all__'