from django.contrib import admin
from .models import Frontend, Backend, AppTech, Language, TechStack


class TechStackAdmin(admin.ModelAdmin):
    list_filter = ['frontend_techs','backend_techs','app_techs','languages']
    search_fields = ['users__nickname','users__full_name','projects__project_name']


admin.site.register(Frontend)
admin.site.register(Backend)
admin.site.register(AppTech)
admin.site.register(Language)
admin.site.register(TechStack, TechStackAdmin)