# Generated by Django 3.0.8 on 2020-08-01 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0016_auto_20200801_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='douban_id',
            new_name='db_id',
        ),
    ]
