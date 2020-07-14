from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Lab, Attendance, Venue


@permission_classes([IsAuthenticated])
class markAttendance(viewsets.ViewSet):
    
    def create(self,request,lab_id):
        get_object_or_404(Venue,pk=lab_id)
        latest_lab = Lab.objects.get(venue=lab_id)
        current_time = datetime.now()

        mark = Attendance.objects.create(attendee=request.user,lab=latest_lab,time_entered=current_time)
        confirmation = AttendanceSerializer(mark)
        return HttpResponse()