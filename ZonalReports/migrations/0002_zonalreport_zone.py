# Generated by Django 5.1 on 2024-08-29 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZonalReports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zonalreport',
            name='zone',
            field=models.TextField(blank=True),
        ),
    ]
