from django.urls import path, include
from rest_framework import routers
from .views import ProjectSerializer, ProjectSerializerForNow

routers = routers.DefaultRouter()
routers.register(r'List', ProjectSerializer)
routers.register(r'list', ProjectSerializerForNow)

urlpatterns = [
    path('', include(routers.urls)),
]