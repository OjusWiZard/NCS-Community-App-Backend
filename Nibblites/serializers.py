from rest_framework import serializers
from Accounts.models import User, Profile, Session
from Projects.serializers import TechStackSerializer


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        exclude = ['id']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id','user']


class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True)
    techstack = TechStackSerializer()
    class Meta:
        model = User
        fields = ['nickname','full_name','profile_pic','email','year','designation','club','phone_no','techstack','profiles']