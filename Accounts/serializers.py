from rest_framework import serializers
from .models import User
from Projects.serializers import TechStackSerializer
from Nibblites.serializers import ProfileSerializer, SessionSerializer


class CurrentuserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True)
    techstack = TechStackSerializer()
    session = SessionSerializer()
    class Meta:
        model = User
        fields = ['nickname','full_name','profile_pic','email','year','session','designation','club','phone_no','techstack','profiles','firebase_token']