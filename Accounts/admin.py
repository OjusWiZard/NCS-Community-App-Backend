from django.contrib import admin
from .models import User, Club, Year, Designation, Session, Branch, Website, Profile, User_links

admin.site.register(User)
admin.site.register(Club)
admin.site.register(Year)
admin.site.register(Designation)
admin.site.register(Session)
admin.site.register(Branch)
admin.site.register(Website)
admin.site.register(Profile)
admin.site.register(User_links)