from rest_framework import serializers
from .models import User, Year, Session, Designation, User_links, Club, Branch
from collections import OrderedDict
from operator import itemgetter


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = ['year']


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        exclude = ['id']


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['club']


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        exclude = ['id']


class User_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_links
        exclude = ['id']

    def to_representation(self, instance):
            excludeNullFields = super().to_representation(instance)
            excludeNullFields = OrderedDict(filter(itemgetter(1), excludeNullFields.items()))
            return excludeNullFields


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ['id']


class UserSerializer(serializers.ModelSerializer):
    user_links = User_linksSerializer()
    class Meta:
        model = User
        fields = ['id','full_name','profile_pic','year','designation','club','phone_no','user_links']