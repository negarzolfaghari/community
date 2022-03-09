# Generated by Django 4.0.2 on 2022-02-28 14:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_company_active_company_date_completion_company_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='last_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=12), size=None),
        ),
    ]