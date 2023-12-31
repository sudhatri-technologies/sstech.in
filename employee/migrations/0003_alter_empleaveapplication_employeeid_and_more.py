# Generated by Django 4.1.5 on 2023-12-16 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_admin', '0002_alter_employee_password_alter_employee_phonenumber_and_more'),
        ('employee', '0002_alter_employeetimeout_employeestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleaveapplication',
            name='employeeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.employee'),
        ),
        migrations.AlterField(
            model_name='employeetimein',
            name='employeeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.employee'),
        ),
        migrations.AlterField(
            model_name='employeetimeout',
            name='employeeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hrm_admin.employee'),
        ),
    ]
