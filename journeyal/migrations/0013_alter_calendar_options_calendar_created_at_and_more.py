# Generated by Django 4.1.4 on 2023-01-03 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journeyal', '0012_journalfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='calendar',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_calendars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_calendars', to=settings.AUTH_USER_MODEL),
        ),
    ]
