# Generated by Django 4.0.4 on 2022-12-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_beds_property_city_property_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='baths',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
