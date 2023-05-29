from rest_framework import generics
from rest_framework import permissions
from apps.clothes.models import Cloth, ClothSampleImage, ClothType, Suit
from apps.clothes.serializers import ClothSerializer, ClothListSerializer, ClothTypeSerializer, SuitSerializer


class ClothesList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of clothes.
    """
    queryset = Cloth.objects.all()
    serializer_class = ClothListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    

class ClothesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single cloth.
    """
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
# class ClothSampleImageList(generics.ListCreateAPIView):
#     """
#     API endpoint that represents a list of sample images of cloth.
#     """
#     queryset = ClothSampleImage.objects.all()
#     serializer_class = ClothSerializer
#     permission_classes = (permissions.IsAuthenticated,)
   
   
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