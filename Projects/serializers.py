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
        fields = ['project_name','project_description','team','current_status','github','deployed_at','icon','background','started_year','last_modified','scope']