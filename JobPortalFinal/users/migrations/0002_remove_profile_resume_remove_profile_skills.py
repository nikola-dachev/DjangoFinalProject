# Generated by Django 5.1.2 on 2024-11-21 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='skills',
        ),
    ]
