# Generated by Django 4.0.5 on 2022-06-25 15:18

from django.db import migrations, models
import functions.models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0015_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_banner',
            field=models.ImageField(blank=True, null=True, upload_to=functions.models.user_picture_directory),
        ),
    ]
