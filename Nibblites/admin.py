from django.contrib import admin
from .models import User, Year, Session, Designation, User_links, Club, Branch, Profiles, Website

admin.site.register(User)
admin.site.register(User_links)
admin.site.register(Profiles)
admin.site.register(Year)
admin.site.register(Session)
admin.site.register(Designation)
admin.site.register(Club)
admin.site.register(Branch)
admin.site.register(Website)