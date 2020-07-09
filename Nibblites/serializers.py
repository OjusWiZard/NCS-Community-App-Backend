from rest_framework import serializers
from Accounts.models import User, Profile, User_links
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
        fields = ['nickname','full_name','profile_pic','email','year','designation','club','phone_no','profiles']


class User_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_links
        exclude = ['id']

    def to_representation(self, instance):
            excludeNullFields = super().to_representation(instance)
            excludeNullFields = OrderedDict(filter(itemgetter(1), excludeNullFields.items()))
            return excludeNullFields


class UserSerializerForNow(serializers.ModelSerializer):
    user_links = User_linksSerializer()
    class Meta:
        model = User
        fields = ['nickname','full_name','profile_pic','email','year','designation','club','phone_no','user_links']