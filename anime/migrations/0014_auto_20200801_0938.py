# Generated by Django 3.0.8 on 2020-08-01 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0013_auto_20200801_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='douban_id',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='publish_y',
            field=models.IntegerField(blank=True, default=1900),
        ),
    ]