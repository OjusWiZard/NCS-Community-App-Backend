from django.contrib.auth.models import Group
from django.db.models import Exists
from Accounts.models import User
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, BasePermission
from .serializers import UserSerializer


class NibbliteViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.filter(groups__name='Nibblite').order_by('designation__rank','-year')
    serializer_class = UserSerializer