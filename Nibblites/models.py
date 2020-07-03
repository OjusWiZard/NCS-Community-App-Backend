from django.db import models

class Year(models.Model):
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.year


class Designation(models.Model):
    designation = models.CharField(max_length=32)

    def __str__(self):
        return self.designation


class Club(models.Model):
    club = models.CharField(max_length=16)

    def __str__(self):
        return self.club


class Session(models.Model):
    session_starting_year = models.PositiveSmallIntegerField()
    session_ending_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.session_starting_year + ' - ' + self.session_ending_year


class User_links(models.Model):
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()
    codechef = models.URLField()
    codeforces = models.URLField()
    hackerrank = models.URLField()
    slack = models.URLField()
    behance = models.URLField()

    def __str__(self):
        return self.user.full_name


class User(models.Model):
    username = models.CharField(max_length=32)
    full_name = models.CharField(max_length=32)
    phone_no = models.CharField(max_length=16)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
    user_links = models.ForeignKey(User_links,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name