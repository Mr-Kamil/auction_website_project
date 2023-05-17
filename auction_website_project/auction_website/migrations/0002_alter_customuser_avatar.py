# Generated by Django 4.2.1 on 2023-05-17 22:10

import auction_website.functions
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('auction_website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[256, 256], upload_to=auction_website.functions.get_avatars_path),
        ),
    ]
