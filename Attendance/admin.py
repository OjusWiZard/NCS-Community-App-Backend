from django.contrib import admin, messages
from django.contrib.auth.models import Group
from django.db.models import Exists, Subquery, Q
from fcm_django.models import FCMDevice
from .models import Announcement, Lab, Attendance, Venue
from Accounts.models import User


def Announce(AnnouncementAdmin,request,queryset):

    for announcement in queryset:
        
        notifyingGroups = Group.objects.filter( id=Exists( announcement.notify_groups.all() ) )
        notifyingUsers = User.objects.filter( Q( groups__in=notifyingGroups ) | Q( id__in=announcement.notify_users.get_queryset() ), is_active=True )
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
    list_display = ['title','message','announcer']
    list_filter = ['notify_groups']
    search_fields = ['announcer__nickname','announcer__full_name','notify_users__nickname','notify_users__full_name']


def Announce_Lab(AnnouncementLab, request, queryset):
    
    notifyingUsers = User.objects.all()
    # notifyingUsers = User.objects.filter( groups='Nibblites', is_active=True )
    notifyingDevices = FCMDevice.objects.filter( user__in=notifyingUsers )

    for lab in queryset:

        lab_title = 'Nibble Lab for ' + lab.topic + ' at ' + str(lab.venue)

        lab_description = 'Lab will start at ' + lab.start_datetime.strftime('%I:%M %p')
        lab_description += ' on ' + lab.start_datetime.strftime('%a, %d %b, %Y') + '.' + '\n'
        lab_description += 'Lab is expected to last for ' + str(lab.duration) + ' hour(s).' + '\n'
        lab_description += lab.additional_info + '\n'
        lab_description += 'Organised by: ' + str(lab.organizer)

        response = notifyingDevices.send_message( title=lab_title, body=lab_description )

        if response:
            successes = response['success']
            failures = response['failure']
            result = 'Announcement Title: ' + lab.topic + ', Successfully Sent: ' + str(response['success']) + ', Failed to Send: ' + str(response['failure'])

            if not response['failure']:
                code = messages.SUCCESS
            elif response['success']>0 and response['failure']>0:
                code = messages.WARNING
            else:
                code = messages.ERROR

            AnnouncementLab.message_user(request, result, code )


class LabAdmin(admin.ModelAdmin):
    actions = [Announce_Lab]
    list_display = ['topic','start_datetime','duration','venue','organizer']
    list_filter = ['venue','organizer']
    list_editable = ['start_datetime','duration','venue','organizer']
    list_per_page = 5
    ordering = ['-start_datetime']
    search_fields = ['topic','organizer__full_name','organizer__nickname']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['attendee','lab','time_entered']
    readonly_fields = ['attendee','lab','time_entered']
    ordering = ['-time_entered']
    search_fields = ['attendee__full_name','attendee__nickname','lab__topic']
    
    def has_add_permission(request, objects=None):
        return False

    def has_delete_permission(self, request, objects=None):
        return False


admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Venue)