# Generated by Django 3.0.8 on 2020-07-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_auto_20200730_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='animation',
            name='douban_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='movie',
            name='douban_id',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='path',
            field=models.FilePathField(allow_folders=True, default=''),
        ),
    ]
