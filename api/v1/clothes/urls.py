from django.urls import path
from .views import ClothesList, ClothesDetail, ClothTypesList, SuitsList

urlpatterns = [
    path('', ClothesList.as_view(), name='clothes_list'),
    path('<int:pk>/', ClothesDetail.as_view(), name='clothes_detail'),
    path('types/', ClothTypesList.as_view(), name='cloth_types_list'),
    path('suits/', SuitsList.as_view(), name='suits_list'),
]