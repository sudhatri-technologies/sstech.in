# Generated by Django 4.1.5 on 2023-12-11 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hrm_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTimeOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('employeeTimeOut', models.TimeField(default=0, null=True)),
                ('employeeWorkDescription', models.TextField(null=True)),
                ('employeeStatus', models.CharField(default='absent', max_length=50)),
                ('employeeId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTimeIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('employeeTimeIn', models.TimeField(default=0, null=True)),
                ('employeeId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmpLeaveApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=100, null=True)),
                ('date', models.DateField()),
                ('reasonForLeave', models.TextField(null=True)),
                ('employeeStatus', models.CharField(default='absent', max_length=50)),
                ('employeeId', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.employee')),
            ],
        ),
    ]
