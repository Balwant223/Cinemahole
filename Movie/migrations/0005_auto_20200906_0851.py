# Generated by Django 3.0.3 on 2020-09-06 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0004_auto_20200828_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='tag',
            new_name='genre',
        ),
    ]
