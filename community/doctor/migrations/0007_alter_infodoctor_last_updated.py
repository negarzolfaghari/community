# Generated by Django 4.0.2 on 2022-03-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_infodoctor_created_infodoctor_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infodoctor',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]