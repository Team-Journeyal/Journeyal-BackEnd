# Generated by Django 4.1.4 on 2022-12-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journeyal', '0004_calendar_notification_rename_sticker_follow_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars'),
        ),
    ]