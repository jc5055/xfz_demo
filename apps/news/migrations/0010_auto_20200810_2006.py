# Generated by Django 2.1.8 on 2020-08-10 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='priority',
            field=models.IntegerField(default=0),
        ),
    ]
