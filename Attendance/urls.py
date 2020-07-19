from django.urls import path, include
from rest_framework import routers
from .views import markAttendance, Schedule

attendanceRouter = routers.DefaultRouter()
attendanceRouter.register(r'', markAttendance, basename='attend')

scheduleRouter = routers.DefaultRouter()
scheduleRouter.register(r'Schedule', Schedule, basename='schedule')

urlpatterns = [
    path('<int:lab_id>/', include(attendanceRouter.urls)),
    path('', include(scheduleRouter.urls)),
]