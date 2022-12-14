from rest_framework import serializers
from .models import User, Calendar, Journal, Notification, Follow

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id', 'name')

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'name')

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'date', 'entry', 'event', 'calendar')

    

