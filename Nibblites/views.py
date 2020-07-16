from Accounts.models import User
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


@permission_classes([IsAuthenticated])
class NibbliteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('designation__rank','-year')
    serializer_class = UserSerializer


class UnsecureNibbliteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('designation__rank','-year')
    serializer_class = UserSerializer