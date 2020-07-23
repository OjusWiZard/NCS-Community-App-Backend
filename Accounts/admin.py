from django.contrib import admin
from .models import User, Website, Profile


admin.site.site_header = 'NCS Community Administration'


class UserAdmin(admin.ModelAdmin):
    exclude = ['password', 'last_login', 'date_joined']
    list_display = ['nickname','designation','year','club','branch','email','phone_no']
    list_filter = ['groups','year','club','branch']
    ordering = ['designation__rank','-year']
    search_fields = ['nickname','full_name']
    fieldsets = (
        (None, {
            'fields': ('nickname','full_name','profile_pic','email','phone_no','year','session','branch')
        }),
        ('For Nibblites', {
            'classes': ('collapse',),
            'fields': ('club','designation','techstack')
        }),
        ('Groups and Permissions', {
            'classes': ('collapse',),
            'fields': ('is_superuser','groups','user_permissions','is_staff','is_active')
        })
    )


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','website','link']
    list_filter = ['website']
    search_fields = ['user__nickname','website__website_name']
    ordering = ['user__designation__rank','-user__year']


admin.site.register(User, UserAdmin)
admin.site.register(Website)
admin.site.register(Profile, ProfileAdmin)