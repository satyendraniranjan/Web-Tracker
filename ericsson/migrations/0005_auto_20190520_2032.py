# Generated by Django 2.0.13 on 2019-05-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ericsson', '0004_auto_20190515_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='ericssonpostcomtracker',
            name='Volte_Soft',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Activity',
            field=models.CharField(blank=True, choices=[('Alarm Report', 'Alarm Report'), ('OSF Recreated', 'OSF Recreated'), ('Troubleshooting', 'Troubleshooting'), ('LATP Testing', 'LATP Testing'), ('FATP Testing', 'FATP Testing'), ('Integration & Testing', 'Integration & Testing'), ('Integration Only', 'Integration Only'), ('Pre - Integration', 'Pre - Integration'), ('LAM', 'LAM')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Activity_status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Pending', 'Pending')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Kpi_Profile',
            field=models.CharField(blank=True, choices=[('Complete', 'Complete'), ('Pending', 'Pending')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Revisit',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Revisit_Required',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Secondary_Fibre_check',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Site_Post_Status',
            field=models.CharField(blank=True, choices=[('Integrated', 'Integrated'), ('Tested', 'Tested')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Site_Pre_Status',
            field=models.CharField(blank=True, choices=[('Integrated', 'Integrated'), ('Ready to integrate', 'Ready to integrate')], max_length=255),
        ),
        migrations.AlterField(
            model_name='ericssonpostcomtracker',
            name='Site_Status_post_Activity',
            field=models.CharField(blank=True, choices=[('Lock', 'Lock'), ('Unlock', 'Unlock')], max_length=255),
        ),
    ]