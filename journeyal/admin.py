from django.contrib import admin
from .models import User, Journal, Calendar, Follow, Notification
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Journal)
admin.site.register(Calendar)
admin.site.register(Follow)
admin.site.register(Notification)


class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
