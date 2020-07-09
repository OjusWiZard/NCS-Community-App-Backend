from .models import Project
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer


@permission_classes([IsAuthenticated])
class ProjectSerializer(viewsets.ModelViewSet):
    queryset = ProjectSerializer.objects.all().order_by('started_year')
    serializer_class = ProjectSerializer


class ProjectSerializerForNow(viewsets.ModelViewSet):
    queryset = ProjectSerializer.objects.all().order_by('started_year')
    serializer_class = ProjectSerializer