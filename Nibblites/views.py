from .models import User, Year, Session, Club, Designation, User_links, Branch
from rest_framework import viewsets
from .serializers import UserSerializer, YearSerializer, SessionSerializer, DesignationSerializer, User_linksSerializer, ClubSerializer, BranchSerializer


class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all().order_by('id')
    serializer_class = BranchSerializer


class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all().order_by('year')
    serializer_class = YearSerializer


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('session_starting_year')
    serializer_class = SessionSerializer


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all().order_by('id')
    serializer_class = DesignationSerializer


class User_linksViewSet(viewsets.ModelViewSet):
    queryset = User_links.objects.all().order_by('id')
    serializer_class = User_linksSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('id')
    serializer_class = ClubSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('designation_id')
    serializer_class = UserSerializer