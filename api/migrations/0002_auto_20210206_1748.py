# Generated by Django 3.1.6 on 2021-02-06 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 17, 48, 8, 364059)),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='headline',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.IntegerField(),
        ),
    ]