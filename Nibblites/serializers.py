from rest_framework import serializers
from .models import User, Year, Session, Designation, User_links, Club, Branch


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = "__all__"


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class User_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_links
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    user_links = User_linksSerializer()
    class Meta:
        model = User
        fields = ['full_name','year','designation','club','phone_no','user_links']