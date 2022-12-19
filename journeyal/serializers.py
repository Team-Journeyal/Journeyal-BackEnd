from rest_framework import serializers
from .models import User, Calendar, Journal, Notification, Follow
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'avatar')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ('id', 'name')


class JournalSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Journal
        fields = ('id', 'date', 'entry', 'event', 'calendar', 'tags')


class CalendarSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True, read_only=True)

    class Meta:
        model = Calendar
        fields = ('id', 'name', 'journals')


class CalendarSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True, read_only=True)

    class Meta:
        model = Calendar
        fields = ('id', 'name', 'journals')
