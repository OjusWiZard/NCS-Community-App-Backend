from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]