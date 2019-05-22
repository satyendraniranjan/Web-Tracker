# Generated by Django 2.0.13 on 2019-02-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracker', '0023_auto_20190301_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='Market',
            field=models.CharField(choices=[('Kansas', 'Kansas'), ('Alaska', 'Alaska'), ('PR / VI', 'PR / VI'), ('DFW', 'DFW'), ('East Texas', 'East Texas'), ('Inland Northwest', 'Inland Northwest'), ('Albuquerque', 'Albuquerque'), ('Jacksonville', 'Jacksonville'), ('Nashville', 'Nashville'), ('West Texas', 'West Texas'), ('Washington DC', 'Washington DC'), ('East Iowa', 'East Iowa'), ('MT / WY', 'MT / WY'), ('South Carolina', 'South Carolina'), ('Riverside / San Bernardino', 'Riverside / San Bernardino'), ('East Kentucky', 'East Kentucky'), ('Alabama', 'Alabama'), ('West Kentucky', 'West Kentucky'), ('Dakotas', 'Dakotas'), ('Orlando', 'Orlando'), ('Central Iowa', 'Central Iowa'), ('Georgia', 'Georgia'), ('Missouri', 'Missouri'), ('Lower Central Valley', 'Lower Central Valley'), ('Atlanta / Athens', 'Atlanta / Athens'), ('Southern Jersey', 'Southern Jersey'), ('Idaho', 'Idaho'), ('LA Metro', 'LA Metro'), ('West Washington', 'West Washington'), ('Orange County', 'Orange County'), ('Oregon / SW Washington', 'Oregon / SW Washington'), ('Mississippi', 'Mississippi'), ('South Texas', 'South Texas'), ('San Antonio', 'San Antonio'), ('Milwaukee', 'Milwaukee'), ('Cincinnati', 'Cincinnati'), ('North Wisconsin', 'North Wisconsin'), ('Rochester', 'Rochester'), ('Houston', 'Houston'), ('Norfolk', 'Norfolk'), ('Miami / West Palm', 'Miami / West Palm'), ('Las Vegas', 'Las Vegas'), ('Cleveland', 'Cleveland'), ('East Michigan', 'East Michigan'), ('Chicago', 'Chicago'), ('SF Bay', 'SF Bay'), ('GA/SC Coast', 'GA/SC Coast'), ('Delaware', 'Delaware'), ('Phoenix', 'Phoenix'), ('West Iowa / Nebraska', 'West Iowa / Nebraska'), ('Pittsburgh', 'Pittsburgh'), ('Central Jersey', 'Central Jersey')], default='', max_length=255),
        ),
    ]