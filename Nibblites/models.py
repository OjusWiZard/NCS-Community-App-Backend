from django.db import models

class Year(models.Model):
    year = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.year)


class Designation(models.Model):
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


class User_links(models.Model):
    email = models.EmailField()
    portfolio = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    codechef = models.URLField(null=True,blank=True)
    codeforces = models.URLField(null=True,blank=True)
    hackerrank = models.URLField(null=True,blank=True)
    hackerearth = models.URLField(null=True,blank=True)
    topcoder = models.URLField(null=True,blank=True)
    codewars = models.URLField(null=True,blank=True)
    leetcode = models.URLField(null=True,blank=True)
    spoj = models.URLField(null=True,blank=True)
    codeingame = models.URLField(null=True,blank=True)
    behance = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.email


class User(models.Model):
    username = models.CharField(max_length=32)
    full_name = models.CharField(max_length=32)
    adminssion_no = models.CharField(max_length=8)
    university_roll_no = models.CharField(max_length=16)
    phone_no = models.CharField(max_length=16)
    club = models.ForeignKey(Club,on_delete=models.CASCADE,to_field='club')
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,to_field='branch_code')
    year = models.ForeignKey(Year,on_delete=models.CASCADE,to_field='year')
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE,to_field='designation')
    user_links = models.OneToOneField(User_links,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name