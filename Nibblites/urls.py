from django.urls import path, include
from rest_framework import routers
from .views import NibbliteViewSet, UnsecureNibbliteViewSet

routers = routers.DefaultRouter()
routers.register(r'unsecuremembers', UnsecureNibbliteViewSet)
routers.register(r'members', NibbliteViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]