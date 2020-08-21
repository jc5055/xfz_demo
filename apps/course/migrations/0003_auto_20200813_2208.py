# Generated by Django 2.1.8 on 2020-08-13 14:08

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_courseorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorder',
            name='id',
        ),
        migrations.AddField(
            model_name='courseorder',
            name='uid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, editable=False, max_length=22, primary_key=True, serialize=False),
        ),
    ]
