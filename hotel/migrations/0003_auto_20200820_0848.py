# Generated by Django 3.1 on 2020-08-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_remove_hotel_available_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='price_per_night',
        ),
        migrations.AddField(
            model_name='hotel',
            name='price_per_night',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19),
        ),
    ]
