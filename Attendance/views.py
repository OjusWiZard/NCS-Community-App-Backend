from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import F
from .models import Lab, Attendance, Venue
from .serializers import ScheduleSerializer

@permission_classes([IsAuthenticated])
class Schedule(viewsets.ModelViewSet):
    queryset = Lab.objects.filter(start_datetime__gte=timezone.now()-F('duration')).order_by(F('start_datetime')+F('duration'))
    serializer_class = ScheduleSerializer


@permission_classes([IsAuthenticated])
class markAttendance(viewsets.ViewSet):
    
    def create(self,request,lab_id):
        get_object_or_404(Venue,pk=lab_id)

        if not Lab.objects.filter(venue=lab_id).last():
            # No lab exist on this venue
            return HttpResponse(status=404)

        else:
            latest_lab = Lab.objects.filter(venue=lab_id).last()
            lab_starting = latest_lab.start_datetime - latest_lab.attendance_offset
            lab_expiry = latest_lab.start_datetime + latest_lab.duration
            current_time = timezone.now()

            if lab_starting <= current_time <= lab_expiry :

                if Attendance.objects.filter(attendee=request.user,lab=latest_lab):
                    # Your attendance is already reported
                    return HttpResponse(status=208)

                else:
                    # Have a nice Lab!
                    Attendance.objects.create(attendee=request.user,lab=latest_lab,time_entered=current_time)
                    return HttpResponse(status=201)

            else:
                # You're either too early or too late
                return HttpResponse(status=410)