# Generated by Django 3.2.5 on 2021-07-25 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lookup', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Model',
            new_name='Recipe',
        ),
    ]