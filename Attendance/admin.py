from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.db.models import Exists, Subquery, Q
from fcm_django.models import FCMDevice
from .models import Announcement, Lab, Attendance, Venue
from Accounts.models import User

def Announce(AnnouncementAdmin,request,queryset):

    for announcement in queryset:
        
        notifyingGroups = Group.objects.filter( id=Exists( announcement.notify_groups.all() ) )
        notifyingUsers = User.objects.filter( Q( groups__in=notifyingGroups ) | Q( id__in=announcement.notify_users.get_queryset() ) )
        notifyingDevices = FCMDevice.objects.filter( user__in=notifyingUsers )

        response = notifyingDevices.send_message( title=announcement.title, body=announcement.message )
        if response:
            successes = response['success']
            failures = response['failure']
            result = 'Announcement Title: ' + announcement.title + ', Successfully Sent: ' + str(response['success']) + ', Failed to Send: ' + str(response['failure'])

            if not response['failure']:
                code = messages.SUCCESS
            elif response['success']>0 and response['failure']>0:
                code = messages.WARNING
            else:
                code = messages.ERROR

            AnnouncementAdmin.message_user(request, result, code )

class AnnouncementAdmin(admin.ModelAdmin):
    actions = [Announce]

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Lab)
admin.site.register(Attendance)
admin.site.register(Venue)