# Generated by Django 4.0.2 on 2022-03-16 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_infodoctor_expertise'),
    ]

    operations = [
        migrations.AddField(
            model_name='infodoctor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='infodoctor',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]