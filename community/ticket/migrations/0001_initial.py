# Generated by Django 4.0.2 on 2022-03-02 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('ticket_id', models.CharField(blank=True, max_length=255)),
                ('user1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thread1_user', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Thread2_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(max_length=1000)),
                ('file', models.FileField(blank=True, upload_to='upload/message_file/')),
                ('status', models.CharField(choices=[('delivered', 'delivered'), ('read', 'read'), ('answerd', 'answerd')], max_length=10)),
                ('direction', models.CharField(choices=[('u1tou2', 'u1tou2'), ('u2tou1', 'u2tou1')], max_length=7)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.thread')),
            ],
        ),
    ]
