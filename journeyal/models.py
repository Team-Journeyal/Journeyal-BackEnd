from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)
    color = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.username


class Calendar(models.Model):
    users = models.ManyToManyField(User, related_name='user_calendars', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_calendars')
    name = models.CharField(max_length=50)
    cal_image = models.ImageField(
        upload_to="cal_covers", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    theme = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.name)


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journals')
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


class JournalImage(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='journal_images')
    image = models.ImageField(upload_to="journal_images", blank=True, null=True)

class JournalFile(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name='journal_files')
    file = models.FileField(upload_to="journal_files", blank=True, null=True)
