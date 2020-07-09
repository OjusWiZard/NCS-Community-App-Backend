from rest_framework import serializers
from .models import Project
from Accounts.models import User


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name']


class ProjectSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True)
    class Meta:
        model = Project
        exclude = ['id']