# Generated by Django 2.1 on 2019-01-28 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0004_auto_20190122_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='data',
            new_name='file',
        ),
    ]