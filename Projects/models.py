from django.db import models
from Accounts.models import User
from Nibblites.models import TechStack

class Project(models.Model):
    project_name = models.CharField(max_length=64)
    project_description = models.CharField(max_length=1024)
    icon = models.ImageField(upload_to='projects/icons/',null=True,blank=True)
    background = models.ImageField(upload_to='projects/backgrounds/',null=True)
    current_status = models.TextField(max_length=64)
    github = models.URLField(blank=True,null=True)
    deployed_at = models.URLField(blank=True,null=True)
    started_year = models.PositiveSmallIntegerField()
    last_modified = models.PositiveSmallIntegerField(blank=True,null=True)
    scope = models.TextField(max_length=1024,blank=True,null=True)
    team = models.ManyToManyField(User,related_name='projects',blank=True)
    techstack = models.ForeignKey(TechStack,on_delete=models.SET_NULL,null=True,related_name='projects')

    def __str__(self):
        return self.project_name