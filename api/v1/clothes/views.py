from rest_framework import generics
from rest_framework import permissions
from apps.clothes.models import Cloth
from apps.clothes.serializers import ClothSerializer, ClothListSerializer


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
    