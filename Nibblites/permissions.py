from Accounts.models import User
from rest_framework.permissions import BasePermission


class IsNibblite(BasePermission):

    def has_permission( self, request, view ):
        nibblites = User.objects.filter(groups__name='Nibblite')
        return request.user in nibblites


class IsAnnouncer(BasePermission):

    def has_permission( self, request, view ):
        announcers = User.objects.filter(groups__name='Announcer')
        return request.user in announcers


class IsModerator(BasePermission):

    def has_permission( self, request, view ):
        moderators = User.objects.filter(groups__name='Moderator')
        return request.user in moderators