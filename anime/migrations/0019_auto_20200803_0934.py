# Generated by Django 3.0.8 on 2020-08-03 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0018_auto_20200801_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animation',
            old_name='douban_id',
            new_name='db_id',
        ),
    ]
