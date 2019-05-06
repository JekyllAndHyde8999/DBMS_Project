# Generated by Django 2.2 on 2019-04-30 19:59

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
            name='Bcamp',
            fields=[
                ('CampId', models.AutoField(primary_key=True, serialize=False)),
                ('CampLocation', models.CharField(max_length=200)),
                ('Address', models.TextField()),
                ('CampStartTime', models.DateTimeField()),
                ('CampStopTime', models.DateTimeField()),
                ('campstatus', models.CharField(default='a', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Bdetails',
            fields=[
                ('FirstName', models.CharField(max_length=40)),
                ('LastName', models.CharField(max_length=40)),
                ('DonorAge', models.IntegerField()),
                ('DonorMobile', models.IntegerField(primary_key=True, serialize=False)),
                ('DonorLocality', models.CharField(max_length=40)),
                ('DonorBgrp', models.TextField(choices=[('A+', 'A-'), ('A-', 'A+'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='O+', max_length=5)),
                ('Donoremail', models.EmailField(max_length=254)),
                ('DonorGender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='NewVolunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vname', models.CharField(max_length=100)),
                ('Vemail', models.EmailField(max_length=254, unique=True)),
                ('Vphone', models.CharField(max_length=11)),
                ('Vstate', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Goa', 'Goa'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('karnataka', 'karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Goa', 'Goa'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Andhra Pradesh', max_length=30)),
                ('Vcity', models.CharField(default='Hyderabad', max_length=200)),
                ('Vlocality', models.CharField(max_length=400)),
                ('Vhouse', models.CharField(max_length=200)),
                ('Vlandmark', models.CharField(max_length=200)),
                ('Vgender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=15)),
                ('Vdate', models.DateTimeField(auto_now_add=True)),
                ('Vblood', models.CharField(choices=[('A+', 'A-'), ('A-', 'A+'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CampId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bcamp.Bcamp')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]