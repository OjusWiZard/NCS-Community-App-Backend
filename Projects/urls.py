from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, ProjectViewSetForNow

routers = routers.DefaultRouter()
routers.register(r'list', ProjectViewSet)
routers.register(r'listall', ProjectViewSetForNow)

urlpatterns = [
    path('', include(routers.urls)),
]