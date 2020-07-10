from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, NibbliteViewSet, UnsecureNibbliteViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'unsecuremembers', UnsecureNibbliteViewSet)
routers.register(r'members', NibbliteViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]