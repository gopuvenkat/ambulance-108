# Generated by Django 2.1.3 on 2018-11-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20181120_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ambulance',
            name='longitude',
            field=models.FloatField(default=0),
        ),
    ]
