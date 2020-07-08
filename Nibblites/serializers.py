from rest_framework import serializers
from Accounts.models import User, Profile
from collections import OrderedDict
from operator import itemgetter


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id','user']


class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True)
    class Meta:
        model = User
        fields = ['full_name','profile_pic','email','year','designation','club','phone_no','profiles']