from django.db import models

class Frontend(models.Model):
    frontend_tech = models.CharField(max_length=64)

    def __str__(self):
        return self.frontend_tech


class Backend(models.Model):
    backend_tech = models.CharField(max_length=64)

    def __str__(self):
        return self.backend_tech


class AppTech(models.Model):
    app_tech = models.CharField(max_length=64)

    def __str__(self):
        return self.app_tech


class Language(models.Model):
    language = models.CharField(max_length=64)

    def __str__(self):
        return self.language


class TechStack(models.Model):
    frontend_techs = models.ManyToManyField(Frontend,blank=True)
    backend_techs = models.ManyToManyField(Backend,blank=True)
    app_techs = models.ManyToManyField(AppTech,blank=True)
    languages = models.ManyToManyField(Language,blank=True)

    def __str__(self):
        if self.users:
            return str(self.users.get(id=1)) + "'s TechStack"
        else:
            return str(self.projects.get(id=1)) + "'s TechStack"