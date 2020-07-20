from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet

routers = routers.DefaultRouter()
routers.register(r'list', ProjectViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]