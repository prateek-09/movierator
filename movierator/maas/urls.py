from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from maas.api.viewsets import MovieViewSet

router = routers.DefaultRouter()

router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# app_name = 'maas'
