# Generated by Django 3.1 on 2020-08-19 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='available_room',
        ),
    ]