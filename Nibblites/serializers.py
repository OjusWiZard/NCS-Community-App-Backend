from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','id','username','full_name','phone_no','year_id','session_id','designation_id','user_links_id']