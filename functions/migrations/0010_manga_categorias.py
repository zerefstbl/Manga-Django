# Generated by Django 4.0.5 on 2022-06-22 18:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0009_remove_manga_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='categorias',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AC', 'Ação'), ('AV', 'Aventura'), ('IS', 'Isekai'), ('FT', 'Fantansia'), ('HT', 'Hentai'), ('EC', 'Ecchi'), ('CT', 'Cultivação')], max_length=20, null=True),
        ),
    ]
