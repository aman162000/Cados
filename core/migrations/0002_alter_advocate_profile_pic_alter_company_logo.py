# Generated by Django 4.1.2 on 2022-10-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='temp-images'),
        ),
    ]
