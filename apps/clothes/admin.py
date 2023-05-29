from django.contrib import admin
from .models import Cloth, ClothType, Suit, ClothSampleImage, ClothModelImage


admin.site.register(Cloth)
admin.site.register(ClothType)
admin.site.register(Suit)
admin.site.register(ClothSampleImage)
admin.site.register(ClothModelImage)
