# Generated by Django 4.0.5 on 2022-06-21 13:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('functions', '0004_manga_banner_alter_manga_capa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='favoritos',
            field=models.ManyToManyField(blank=True, null=True, related_name='favoritados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manga',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]