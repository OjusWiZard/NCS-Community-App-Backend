from django.db import models
from django.db.models import QuerySet
from django.utils import timezone
from django.contrib.auth.models import Group
from fcm_django.models import FCMDevice
from Accounts.models import User


class Venue(models.Model):
    venue_name = models.CharField(max_length=64)

    def __str__(self):
        return self.venue_name


class Lab(models.Model):
    start_datetime = models.DateTimeField()
    attendance_offset = models.DurationField(default=timezone.timedelta(minutes=5))
    duration = models.DurationField(default=timezone.timedelta(hours=2))
    topic = models.CharField(max_length=64)
    additional_info = models.TextField(max_length=512,null=True,blank=True)
    venue = models.ForeignKey(Venue,on_delete=models.SET_NULL,null=True)
    organizer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='labs_organized')
    attendees = models.ManyToManyField(User,through='Attendance',related_name='labs_attended')

    def __str__(self):
        return self.topic


class Attendance(models.Model):
    attendee = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    lab = models.ForeignKey(Lab,on_delete=models.SET_NULL,null=True)
    time_entered = models.DateTimeField()

    def __str__(self):
        return str(self.attendee) + ' in ' + str(self.lab)


class Announcement(models.Model):
    title = models.CharField(max_length=64)
    message = models.TextField(max_length=512)
    announcer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='announcements')
    notify_groups = models.ManyToManyField(Group,blank=True)
    notify_users = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title