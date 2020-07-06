"""NCSApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, YearViewSet, ClubViewSet, User_linksViewSet, SessionViewSet, DesignationViewSet, BranchViewSet, ProfilesViewSet

routers = routers.DefaultRouter()
routers.register(r'users', UserViewSet)
routers.register(r'years', YearViewSet)
routers.register(r'clubs', ClubViewSet)
routers.register(r'branch', BranchViewSet)
routers.register(r'sessions', SessionViewSet)
routers.register(r'designations', DesignationViewSet)
routers.register(r'user_linkss', User_linksViewSet)
routers.register(r'profiles', ProfilesViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]