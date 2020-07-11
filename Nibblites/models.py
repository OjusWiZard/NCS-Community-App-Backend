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
    frontend_stack = models.ManyToManyField(Frontend,blank=True)
    backend_stack = models.ManyToManyField(Backend,blank=True)
    app_tech_stack = models.ManyToManyField(AppTech,blank=True)
    languages = models.ManyToManyField(Language,blank=True)