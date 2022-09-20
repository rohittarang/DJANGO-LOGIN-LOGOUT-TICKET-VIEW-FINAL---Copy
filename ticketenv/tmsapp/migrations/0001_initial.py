# Generated by Django 4.1.1 on 2022-09-18 12:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(default='000001', editable=False, max_length=8)),
                ('server_details', models.CharField(max_length=100)),
                ('send_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('license_no', models.CharField(max_length=25)),
                ('file', models.FileField(upload_to='documents/%Y%m%d/')),
            ],
        ),
    ]