# Generated by Django 2.1.2 on 2018-11-18 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181117_0722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='name',
        ),
    ]
