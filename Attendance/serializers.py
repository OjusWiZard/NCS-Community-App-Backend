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
    class Meta:
        model = Lab
        fields = ['start_datetime','attendance_offset','duration','topic','additional_info','venue','organizer','attendees']