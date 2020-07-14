from django.urls import path, include
from rest_framework import routers
from .views import markAttendance

routers = routers.DefaultRouter()
routers.register(r'', markAttendance, basename='attend')

urlpatterns = [
    path('<int:lab_id>/', include(routers.urls)),
]