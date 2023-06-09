from rest_framework import generics
from rest_framework import permissions
from apps.clothes.models import Cloth, ClothSampleImage, ClothType, Suit, ClothModelImage
from apps.clothes.serializers import ClothSerializer, ClothListSerializer, ClothTypeSerializer, SuitSerializer, ClothSampleImageSerializer, ClothModelImageSerializer
import os


class ClothesList(generics.ListAPIView):
    """
    API endpoint that represents a list of clothes.
    """
    queryset = Cloth.objects.all()
    serializer_class = ClothListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
class ClothesCreate(generics.CreateAPIView):
    """
    API endpoint to create a new cloth
    """
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    permission_classes = (permissions.IsAuthenticated,)
    

class ClothesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single cloth.
    """
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def perform_destroy(self, instance):
        image = instance.image
        
        if image:
            image_path = image.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
                
        image.delete()
        
        return super().perform_destroy(instance)
    
   
class ClothTypesList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of cloth types.
    """
    queryset = ClothType.objects.all()
    serializer_class = ClothTypeSerializer
    permission_classes = (permissions.IsAuthenticated,) 
    
class SuitsList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of suits.
    """
    queryset = Suit.objects.all()
    serializer_class = SuitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    

class ClothSampleImageCreate(generics.CreateAPIView):
    """
    API endpoint to create a new cloth sample image
    """
    queryset = ClothSampleImage.objects.all()
    serializer_class = ClothSampleImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    
class ClothModelImageCreate(generics.CreateAPIView):
    """
    API endpoint to create a new cloth model image
    """
    queryset = ClothModelImage.objects.all()
    serializer_class = ClothModelImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
class ClothModelImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single cloth model image.
    """
    queryset = ClothModelImage.objects.all()
    serializer_class = ClothModelImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.image:
            image_path = instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.image:
            image_path = instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
                
        return super().destroy(request, *args, **kwargs)
            

class ClothSampleImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single cloth sample image.
    """
    queryset = ClothSampleImage.objects.all()
    serializer_class = ClothSampleImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.image:
            image_path = instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.image:
            image_path = instance.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
                
        return super().destroy(request, *args, **kwargs)