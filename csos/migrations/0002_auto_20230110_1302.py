# Generated by Django 4.1.4 on 2023-01-10 10:02

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('csos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cso',
            name='date_published',
            field=models.DateTimeField(auto_now_add=True,verbose_name="date_published"),
        ),
        migrations.AddField(
            model_name='cso',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True,verbose_name="date_updated"),
        ),
    ]
