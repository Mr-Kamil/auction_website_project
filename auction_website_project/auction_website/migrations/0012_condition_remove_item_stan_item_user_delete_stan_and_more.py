# Generated by Django 4.2.1 on 2023-05-13 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction_website', '0011_alter_account_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='stan',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auction_website.account'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Stan',
        ),
        migrations.AddField(
            model_name='item',
            name='condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auction_website.condition'),
        ),
    ]
