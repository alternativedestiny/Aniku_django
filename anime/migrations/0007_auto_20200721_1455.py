# Generated by Django 3.0.8 on 2020-07-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_auto_20200721_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]