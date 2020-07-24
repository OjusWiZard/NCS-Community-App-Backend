from django.contrib import admin, messages
from django.contrib.auth.models import Group
from .models import User, Website, Profile, Designation


admin.site.site_header = 'NCS Community Administration'


def make_Nibblite( UserAdmin, request, queryset ):

    if not request.user.is_superuser:
        UserAdmin.message_user( request, 'You are NOT a SuperUser', messages.ERROR )
        
    else:
        nibblites = Group.objects.get(name='Nibblite')
        member = Designation.objects.get(designation='Member')
        for user in queryset:
            nibblites.user_set.add(user)
            user.designation = member
            user.save()
        UserAdmin.message_user( request, 'Congratulations to the new Nibblites!!! 🥳', messages.SUCCESS )


def make_Moderator( UserAdmin, request, queryset ):

    if not request.user.is_superuser:
        UserAdmin.message_user( request, 'You are NOT a SuperUser', messages.ERROR )

    else:
        moderator = Group.objects.get(name='Moderator')
        for user in queryset:
            moderator.user_set.add(user)
            user.is_staff = True
            user.save()
        UserAdmin.message_user( request, 'New Moderators added', messages.SUCCESS )


def make_Announcer( UserAdmin, request, queryset ):

    if not request.user.is_superuser:
        UserAdmin.message_user( request, 'You are NOT a SuperUser', messages.ERROR )

    else:
        announcer = Group.objects.get(name='Announcer')
        for user in queryset:
            announcer.user_set.add(user)
            user.is_staff = True
            user.save()
        UserAdmin.message_user( request, 'New Announcers added', messages.SUCCESS )


class UserAdmin(admin.ModelAdmin):  
    actions = [make_Nibblite, make_Announcer, make_Moderator]
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