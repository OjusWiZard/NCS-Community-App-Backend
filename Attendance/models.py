from django.db import models
from django.db.models import QuerySet
from django.db.models import F
from django.core.exceptions import ValidationError
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
    topic = models.CharField(max_length=25) # Notification Title may overflow beyond 25
    additional_info = models.TextField(max_length=245,null=True,blank=True) # Notification Body may overflow beyond 245
    venue = models.ForeignKey(Venue,on_delete=models.SET_NULL,null=True)
    organizer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='labs_organized')
    attendees = models.ManyToManyField(User,through='Attendance',related_name='labs_attended')

    def clean(self):
        previous_lab = Lab.objects.filter(start_datetime__lt=self.start_datetime).order_by(F('start_datetime') + F('duration')).last()
        next_lab = Lab.objects.filter(start_datetime__gt=self.start_datetime).order_by(F('start_datetime') + F('duration')).first()
        if (previous_lab is not None):
            if (previous_lab.start_datetime + previous_lab.duration > self.start_datetime and self.venue == previous_lab.venue):
                print('The Lab is overlapping with the previous Lab: '+str(previous_lab)+'!')
                raise ValidationError('The Lab is overlapping with the previous Lab: '+str(previous_lab)+'!')
        if (next_lab is not None):
            if (self.start_datetime + self.duration > next_lab.start_datetime and self.venue == previous_lab.venue):
                print('The Lab is overlapping with the next Lab: '+str(next_lab)+'!')
                raise ValidationError('The Lab is overlapping with the next Lab: '+str(next_lab)+'!')

    def save(self, *args, **kwargs):
        super(Lab, self).save(*args, **kwargs)
        Attendance.objects.create(attendee=self.organizer,lab=self,time_entered=self.start_datetime)

    def __str__(self):
        return self.topic


class Attendance(models.Model):
    attendee = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    lab = models.ForeignKey(Lab,on_delete=models.SET_NULL,null=True)
    time_entered = models.DateTimeField()

    def __str__(self):
        return str(self.attendee) + ' was in ' + str(self.lab)


class Announcement(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=365)
    announcer = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='announcements')
    notify_groups = models.ManyToManyField(Group,blank=True)
    notify_users = models.ManyToManyField(User,blank=True)

    def __str__(self):
        return self.title