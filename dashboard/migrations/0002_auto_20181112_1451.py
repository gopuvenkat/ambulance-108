# Generated by Django 2.1.3 on 2018-11-12 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=15)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('contact_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_latitude', models.FloatField()),
                ('start_longitude', models.FloatField()),
                ('ambulance_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Ambulance')),
            ],
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='location',
        ),
        migrations.AddField(
            model_name='hospital',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='hospital_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Hospital'),
        ),
        migrations.AddField(
            model_name='trip',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Patient'),
        ),
    ]
