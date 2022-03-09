# Generated by Django 4.0.2 on 2022-02-19 13:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6)),
                ('father_name', models.CharField(max_length=50)),
                ('birth_place', models.CharField(max_length=50)),
                ('place_issuance_identitycard', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('identity_number', models.CharField(max_length=1000)),
                ('identity_serial_number', models.CharField(max_length=1000)),
                ('national_code', models.CharField(max_length=100)),
                ('education', models.CharField(choices=[('bisavad', 'bisavad'), ('sicl', 'sicl'), ('diplom', 'diplom'), ('kardani', 'kardani'), ('karshenasi', 'karshenasi'), ('karshenasiarshad', 'karshenasiarshad'), ('doctora', 'doctora')], max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('work_address', models.CharField(max_length=1000)),
                ('locations', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('home_address', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=11)),
                ('phone_number', models.CharField(max_length=10)),
                ('aviculter_address', models.CharField(max_length=1000)),
                ('postalcode', models.CharField(max_length=100)),
                ('township', models.CharField(max_length=100)),
            ],
        ),
    ]
