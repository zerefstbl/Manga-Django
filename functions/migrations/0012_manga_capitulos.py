# Generated by Django 4.0.5 on 2022-06-24 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0011_alter_profile_favoritos'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='capitulos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='capitulos_totais', to='functions.newcap'),
        ),
    ]
