# Generated by Django 2.0.13 on 2019-04-12 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0052_auto_20190413_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='Assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]
