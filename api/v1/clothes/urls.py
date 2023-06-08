from django.urls import path
from .views import ClothesList, ClothesDetail, ClothTypesList, SuitsList, ClothesCreate, ClothSampleImageCreate, ClothModelImageCreate

urlpatterns = [
    path('', ClothesList.as_view(), name='clothes_list'),
    path('create/', ClothesCreate.as_view(), name='clothes_create'),
    path('create/sample_image/', ClothSampleImageCreate.as_view(), name='cloth_sample_image_create'),
    path('create/model_image/', ClothModelImageCreate.as_view(), name='cloth_model_image_create'),
    path('types/', ClothTypesList.as_view(), name='cloth_types_list'),
    path('suits/', SuitsList.as_view(), name='suits_list'),
    path('<str:pk>/', ClothesDetail.as_view(), name='clothes_detail'),
]