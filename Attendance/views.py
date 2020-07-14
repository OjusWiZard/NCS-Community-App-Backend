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

        if not Lab.objects.filter(venue=lab_id).last():
            return HttpResponse(status=404)

        latest_lab = Lab.objects.filter(venue=lab_id).last()
        current_time = datetime.now()

        if Attendance.objects.filter(attendee=request.user,lab=latest_lab):
            return HttpResponse(status=208)

        Attendance.objects.create(attendee=request.user,lab=latest_lab,time_entered=current_time)
        return HttpResponse(status=201)