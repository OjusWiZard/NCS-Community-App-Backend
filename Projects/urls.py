from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, ProjectViewSetForNow

routers = routers.DefaultRouter()
routers.register(r'List', ProjectViewSet)
routers.register(r'list', ProjectViewSetForNow)

urlpatterns = [
    path('', include(routers.urls)),
]