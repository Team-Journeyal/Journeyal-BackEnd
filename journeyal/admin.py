from django.contrib import admin
from .models import User, Journal, Event, Tag, Sticker
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Journal)
admin.site.register(Event)
admin.site.register(Tag)
admin.site.register(Sticker)
