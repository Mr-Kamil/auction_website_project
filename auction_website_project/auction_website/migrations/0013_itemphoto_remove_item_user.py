# Generated by Django 4.2.1 on 2023-05-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_website', '0012_condition_remove_item_stan_item_user_delete_stan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]
