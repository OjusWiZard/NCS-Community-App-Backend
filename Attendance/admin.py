from django.contrib import admin
from fcm_django.models import FCMDevice
from .models import Announcement, Lab, Attendance, Venue

def Announce(Announcement,request,queryset):

    announcements = list(queryset)
    notifyingGroups = [ group for announcement in announcements for group in list( announcement.notify_groups.all() ) ] # Very UGLY way to get all groups from all announcements
    notifyingUsers = [ user for group in notifyingGroups for user in list( group.user_set.all() ) ] # Very UGLY way to get all users from all groups
    notifyingUsers += [ user for announcement in announcements for user in list( announcement.notify_users.all() ) ] # Very UGLY way to append all users from all announcements
    notifyingDevices = [ device for user in notifyingUsers for device in list( user.fcmdevice_set.all() ) ] # Very UGLY way to get all devices of all users

    for device in notifyingDevices:
        device.send_message("Title", "Message")
        print("sending to "+str(device))

class AnnouncementAdmin(admin.ModelAdmin):
    actions = [Announce]

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Lab)
admin.site.register(Attendance)
admin.site.register(Venue)