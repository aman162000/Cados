# Generated by Django 4.1.2 on 2022-10-25 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_advocate_link_link_advocate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='core.company'),
        ),
    ]