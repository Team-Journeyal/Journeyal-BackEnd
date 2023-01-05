from rest_framework import serializers
from .models import User, Calendar, Journal, JournalImage, JournalFile, Notification, Follow
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'avatar', 'username', 'color')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)


class JournalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalImage
        fields = ['id', 'image']


class JournalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalFile
        fields = ['id', 'file']


class JournalSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    journal_images = JournalImageSerializer(many=True, read_only=True)
    journal_files = JournalFileSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=True, use_url=False), write_only=True, required=False)
    uploaded_files = serializers.ListField(
        child=serializers.FileField(
            max_length=1000000, allow_empty_file=True, use_url=False), write_only=True, required=False)

    class Meta:
        model = Journal
        fields = ('id', 'date', 'user', 'entry', 'event', 'calendar', 'tags','journal_images', 'uploaded_images', 'journal_files', 'uploaded_files')

    def create(self, validated_data):
        if 'uploaded_images' in validated_data.keys():
            uploaded_images = validated_data.pop('uploaded_images')
            journal = super().create(validated_data)
            for image in uploaded_images:
                JournalImage.objects.create(journal=journal, image=image)
            return journal

        else:
            return super().create(validated_data)
        
    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', None)
        uploaded_files = validated_data.pop('uploaded_files', None)
        if uploaded_images:
            # self.clear_existing_images(instance) # if we want to clear existing images.
            journal_image_model_instance = [JournalImage(
                journal=instance, image=image) for image in uploaded_images]
            JournalImage.objects.bulk_create(
                journal_image_model_instance
            )
        if uploaded_files:
            journal_file_model_instance = [JournalFile(
                journal=instance, file=file) for file in uploaded_files]
            JournalFile.objects.bulk_create(
                journal_file_model_instance
            )
        return super().update(instance, validated_data)


class CalendarUsernameSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True, read_only=True)
    owner = serializers.SlugRelatedField(slug_field="username", many=False, read_only=True)
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Calendar
        fields = ('id', 'owner', 'users', 'name','cal_image', 'created_at', 'theme', 'journals',)


class CalendarSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True, read_only=True)
    owner = serializers.SlugRelatedField(slug_field="username", many=False, read_only=True)
    

    class Meta:
        model = Calendar
        fields = ('id', 'owner', 'users', 'name', 'cal_image', 'created_at', 'theme', 'journals',)

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.cal_image.save(file.name, file, save=True)
            return instance
        return super().update(instance, validated_data)
