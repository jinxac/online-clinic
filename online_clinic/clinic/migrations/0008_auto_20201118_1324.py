# Generated by Django 3.1.3 on 2020-11-18 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_auto_20201118_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeerole',
            old_name='role_id',
            new_name='role',
        ),
    ]