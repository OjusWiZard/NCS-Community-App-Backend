from django.contrib import admin
from .models import Frontend, Backend, AppTech, Language, TechStack

admin.site.register(Frontend)
admin.site.register(Backend)
admin.site.register(AppTech)
admin.site.register(Language)
admin.site.register(TechStack)