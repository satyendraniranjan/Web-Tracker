# Generated by Django 2.0.13 on 2019-03-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0028_shippinginfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='User_Name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='cascade',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]