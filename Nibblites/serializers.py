from rest_framework import serializers
from .models import User, User_links, Profiles
from collections import OrderedDict
from operator import itemgetter


class User_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_links
        exclude = ['id']

    def to_representation(self, instance):
            excludeNullFields = super().to_representation(instance)
            excludeNullFields = OrderedDict(filter(itemgetter(1), excludeNullFields.items()))
            return excludeNullFields


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        exclude = ['id','user']


class UserSerializer(serializers.ModelSerializer):
    user_links = User_linksSerializer()
    profiles = ProfileSerializer(many=True)
    class Meta:
        model = User
        fields = ['full_name','profile_pic','email','year','designation','club','phone_no','user_links','profiles']