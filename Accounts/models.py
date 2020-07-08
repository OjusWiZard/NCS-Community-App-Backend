from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import UserManager


class Year(models.Model):
    year = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.year)


class Designation(models.Model):
    rank = models.PositiveSmallIntegerField()
    designation = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.designation


class Club(models.Model):
    club = models.CharField(max_length=16,unique=True)

    def __str__(self):
        return self.club


class Session(models.Model):
    session_starting_year = models.PositiveSmallIntegerField()
    session_ending_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.session_starting_year) + ' - ' + str(self.session_ending_year)


class Branch(models.Model):
    branch_code = models.CharField(max_length=8, unique=True)
    branch_full_form = models.CharField(max_length=64)

    def __str__(self):
        return self.branch_code


class Website(models.Model):
    website_name = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.website_name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    username = models.CharField(max_length=32)
    profile_pic = models.ImageField(upload_to='profile_pictures/',blank=True,null=True)
    full_name = models.CharField(max_length=32)
    phone_no = models.CharField(max_length=16)
    club = models.ForeignKey(Club,on_delete=models.CASCADE,to_field='club')
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,to_field='branch_code')
    year = models.ForeignKey(Year,on_delete=models.CASCADE,to_field='year')
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,to_field='designation')
    profiles = models.ManyToManyField(Website,through='Profile',null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','full_name','phone_no','club','branch','year','session','designation']

    objects = UserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    website = models.ForeignKey(Website,on_delete=models.CASCADE,to_field='website_name')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    link = models.URLField()

    def __str__(self):
        return "'s ".join([str(self.user),str(self.website)])