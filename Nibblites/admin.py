from django.contrib import admin
from .models import User, Year, Session, Designation, User_links, Club

admin.site.register(User)
admin.site.register(User_links)
admin.site.register(Year)
admin.site.register(Session)
admin.site.register(Designation)
admin.site.register(Club)