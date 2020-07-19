from rest_framework import serializers
from .models import Lab, Venue
from Projects.serializers import TeamSerializer


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['venue_name']


class ScheduleSerializer(serializers.ModelSerializer):
    attendees = TeamSerializer(many=True)
    organizer = TeamSerializer()
    venue = VenueSerializer()
    start_date = serializers.SerializerMethodField('custom_date')
    start_time = serializers.SerializerMethodField('custom_time')

    def custom_date(self, lab):
        return lab.start_datetime.strftime('%a, %d %b, %Y')
    
    def custom_time(self, lab):
        return lab.start_datetime.strftime('%I:%M %p')

    class Meta:
        model = Lab
        fields = ['start_date','start_time','attendance_offset','duration','topic','additional_info','venue','organizer','attendees']