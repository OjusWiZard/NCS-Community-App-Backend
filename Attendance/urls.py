from django.urls import path, include
from .views import markAttendance

urlpatterns = [
    path('<int:venue>', markAttendance, name='attend')
]