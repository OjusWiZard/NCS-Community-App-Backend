from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import F
from .models import Lab, Attendance, Venue
from .serializers import ScheduleSerializer
from Nibblites.permissions import IsNibblite


class Schedule(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated,IsNibblite]
    queryset = Lab.objects.filter(start_datetime__gte=timezone.now()-F('duration')-timezone.timedelta(days=0)).order_by(F('start_datetime')+F('duration'))
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        days_offset = 0
        if self.request.query_params.get('days'):
            days_offset = int(self.request.query_params.get('days'))
        updated_queryset = Lab.objects.filter(start_datetime__gte=timezone.now()-F('duration')-timezone.timedelta(days=days_offset)).order_by(F('start_datetime')+F('duration'))
        return updated_queryset


class markAttendance(viewsets.ViewSet):
    permission_classes = [IsAuthenticated,IsNibblite]
    
    def create(self,request,venue_id):
        get_object_or_404(Venue,pk=venue_id)

        if not Lab.objects.filter(venue=venue_id).last():
            # No lab exist on this venue
            return HttpResponse(status=404)

        else:
            target_lab = Lab.objects.filter(venue=venue_id,start_datetime__gte=timezone.now()-F('duration')).order_by(F('start_datetime')+F('duration')).first()
            
            if not target_lab:
                return HttpResponse(status=410)

            lab_starting = target_lab.start_datetime - target_lab.attendance_offset
            lab_expiry = target_lab.start_datetime + target_lab.duration
            current_time = timezone.now()

            if lab_starting <= current_time <= lab_expiry :

                if Attendance.objects.filter(attendee=request.user,lab=target_lab):
                    # Your attendance is already reported
                    return HttpResponse(status=208)

                else:
                    # Have a nice Lab!
                    Attendance.objects.create(attendee=request.user,lab=target_lab,time_entered=current_time)
                    return HttpResponse(status=201)

            else:
                # You're either too early or too late
                return HttpResponse(status=410)