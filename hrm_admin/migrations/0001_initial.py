# Generated by Django 4.1.5 on 2023-01-04 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('fatherName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dOB', models.DateField()),
                ('phoneNumber', models.IntegerField()),
                ('maritialStatus', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('localAddress', models.TextField()),
                ('permanentAddress', models.TextField()),
                ('employeeId', models.CharField(max_length=100)),
                ('shift', models.CharField(max_length=100)),
                ('dOJ', models.DateField()),
                ('isAdmin', models.BooleanField(default=False)),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.department')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.position')),
            ],
        ),
    ]