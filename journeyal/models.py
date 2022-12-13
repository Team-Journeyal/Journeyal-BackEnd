from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    # avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)

class Day(models.Model):
    date = models.DateField()
    journal = models.TextField(null=True, blank=True)
    # image = models.TextField(null=True, blank=True)
    stickers = models.ManyToManyField('Sticker')
    tags = models.ManyToManyField('Tag')
    
    def __str__(self):
        return self.date

class Event(models.Model):
    name = models.CharField(max_length=100)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Sticker(models.Model):
    pass
    # image = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)