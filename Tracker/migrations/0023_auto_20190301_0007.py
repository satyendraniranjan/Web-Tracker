# Generated by Django 2.0.13 on 2019-02-28 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0022_auto_20190223_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
    ]
