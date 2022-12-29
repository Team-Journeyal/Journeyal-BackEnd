from rest_framework import serializers
from .models import User, Calendar, Journal, JournalImage, Notification, Follow
from taggit.serializers import (TagListSerializerField, TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'avatar', 'username')

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


class JournalSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    journal_images = JournalImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(
            max_length=1000000, allow_empty_file=True, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Journal
        fields = ('id', 'date', 'entry', 'event', 'calendar',
                  'tags', 'journal_images', 'uploaded_images', 'user')

    # def create(self, validated_data):
    #     uploaded_images = validated_data.pop('uploaded_images')
    #     journal = Journal.objects.create(**validated_data)
    #     for image in uploaded_images:
    #         JournalImage.objects.create(journal=journal, image=image)
    #     return journal

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', None)
        if uploaded_images:
            # self.clear_existing_images(instance) # if we want to clear existing images.
            journal_image_model_instance = [JournalImage(
                journal=instance, image=image) for image in uploaded_images]
            JournalImage.objects.bulk_create(
                journal_image_model_instance
            )
        return super().update(instance, validated_data)


class CalendarSerializer(serializers.ModelSerializer):
    journals = JournalSerializer(many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Calendar
        fields = ('id', 'owner', 'users', 'name', 'cal_image', 'journals')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.cal_image.save(file.name, file, save=True)
            return instance
        return super().update(instance, validated_data)
