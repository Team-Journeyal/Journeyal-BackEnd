from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    # avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)


class Journal(models.Model):
    date = models.DateField()
    entry = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.date)


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Sticker(models.Model):
    pass
    # date = models.DateField()
    # image = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

# add image down here
