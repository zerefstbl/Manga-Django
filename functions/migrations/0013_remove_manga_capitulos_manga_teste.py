# Generated by Django 4.0.5 on 2022-06-24 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0012_manga_capitulos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manga',
            name='capitulos',
        ),
        migrations.AddField(
            model_name='manga',
            name='teste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='testezin', to='functions.newcap'),
        ),
    ]