from django.contrib import admin
from .models import User, Journal, Calendar, Follow, Notification
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Journal)
admin.site.register(Calendar)
admin.site.register(Follow)
admin.site.register(Notification)
