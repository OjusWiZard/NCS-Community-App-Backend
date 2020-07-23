from .models import Project
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer


@permission_classes([IsAuthenticated])
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(show_in_app=True).order_by('-last_modified')
    serializer_class = ProjectSerializer