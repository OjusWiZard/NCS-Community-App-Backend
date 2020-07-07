from django.db import models

class Year(models.Model):
    year = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.year)


class Designation(models.Model):
    rank = models.PositiveSmallIntegerField(null=True)
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


class User(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_pictures/',blank=True)
    full_name = models.CharField(max_length=32)
    adminssion_no = models.CharField(max_length=8)
    university_roll_no = models.CharField(max_length=16)
    phone_no = models.CharField(max_length=16)
    club = models.ForeignKey(Club,on_delete=models.CASCADE,to_field='club')
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,to_field='branch_code')
    year = models.ForeignKey(Year,on_delete=models.CASCADE,to_field='year')
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,to_field='designation')

    def __str__(self):
        return self.full_name


class Profiles(models.Model):
    website = models.ForeignKey(Website,on_delete=models.CASCADE,to_field='website_name')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='profiles')
    link = models.URLField()

    def __str__(self):
        return "'s ".join([str(self.user),str(self.website)])