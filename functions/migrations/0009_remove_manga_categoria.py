# Generated by Django 4.0.5 on 2022-06-22 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0008_remove_manga_favoritos_profile_favoritos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='categoria',
        ),
    ]