# Generated by Django 2.1.15 on 2020-10-14 13:06

from django.db import migrations, models
import restaurants.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restauraunt_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restauraunt',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='restauraunt',
            name='logo',
            field=models.ImageField(null=True, upload_to=restaurants.models.upload_logo),
        ),
    ]
