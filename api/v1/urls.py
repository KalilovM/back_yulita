from django.urls import include, path

urlpatterns = [
    path("users/", include("api.v1.users.urls")),
    path("clothes/", include("api.v1.clothes.urls")),
]
