from rest_framework import serializers
from .models import Project
from Accounts.models import User
from Nibblites.models import Frontend, Backend, AppTech, Language, TechStack


class FrontendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frontend
        fields = ['frontend_tech']


class BackendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backend
        fields = ['backend_tech']


class AppTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppTech
        fields = ['app_tech']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language']


class TechStackSerializer(serializers.ModelSerializer):
    frontend_techs = FrontendSerializer(many=True,read_only=True)
    backend_techs = BackendSerializer(many=True,read_only=True)
    app_techs = AppTechSerializer(many=True,read_only=True)
    languages = LanguageSerializer(many=True,read_only=True)

    class Meta:
        model = TechStack
        fields = ['languages','frontend_techs','backend_techs','app_techs']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name']


class ProjectSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True)
    techstack = TechStackSerializer()
    class Meta:
        model = Project
        fields = ['project_name','project_description','team','techstack','current_status','github','deployed_at','icon','background','started_year','last_modified','scope']