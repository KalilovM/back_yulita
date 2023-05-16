from django.urls import path
from .views import ClothesList, ClothesDetail

urlpatterns = [
    path('', ClothesList.as_view(), name='clothes_list'),
    path('<int:pk>/', ClothesDetail.as_view(), name='clothes_detail'),
]