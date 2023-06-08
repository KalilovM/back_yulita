from rest_framework import serializers

from .models import Cloth, ClothType, Suit, ClothSampleImage, ClothModelImage


class ClothSerializer(serializers.ModelSerializer):
    model_images = serializers.SerializerMethodField()
    sample_images = serializers.SerializerMethodField()
    class Meta:
        model = Cloth
        fields = '__all__'
        
    def get_model_images(self, obj):
        request = self.context.get('request')
        images = obj.model_images.all()
        if images:
            return [{'id': image.id, 'image': request.build_absolute_uri(image.image.url)} for image in images]
        
    def get_sample_images(self, obj):
        request = self.context.get('request')
        images = obj.sample_images.all()
        if images:
            return [{'id': image.id, 'image': request.build_absolute_uri(image.image.url)} for image in images]


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
        
        
class ClothSampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothSampleImage
        fields = '__all__'
        
        
class ClothModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothModelImage
        fields = '__all__'