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
    cal_image = models.ImageField(
        upload_to="cal_covers", blank=True, null=True)
    theme = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Journal(models.Model):
    calendar = models.ForeignKey(
        Calendar, on_delete=models.CASCADE, related_name='journals')
    date = models.DateField()
    entry = models.TextField(null=True, blank=True)
    event = models.CharField(max_length=200, null=True, blank=True)
    tags = TaggableManager(blank=True)



def __str__(self):
    return str(self.date)


class Notification(models.Model):
    pass


class Follow(models.Model):
    pass


# class JournalImage(models.Model):
#     journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='journal_images')
#     image = models.ImageField(upload_to="journal_images", blank=True, null=True)
