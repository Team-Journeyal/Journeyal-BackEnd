from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)

    def __str__(self):
        return self.username


class Calendar(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='calendars')
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Journal(models.Model):
    calendar = models.ForeignKey(
        Calendar, on_delete=models.CASCADE, related_name='journals')
    date = models.DateField()
    entry = models.TextField(null=True, blank=True)
    event = models.CharField(max_length=200, null=True, blank=True)

    # image = models.ImageField(null=True, blank=True)
    tags = TaggableManager()
# stickers =


def __str__(self):
    return str(self.date)


class Notification(models.Model):
    pass


class Follow(models.Model):
    pass
