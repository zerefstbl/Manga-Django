# Generated by Django 4.0.5 on 2022-06-22 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0010_manga_categorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favoritos',
            field=models.ManyToManyField(blank=True, null=True, related_name='favoritados', to='functions.manga'),
        ),
    ]