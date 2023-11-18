from django.db import models

# Create your models here.
class EmployeeTimeIn(models.Model):
    employeeName=models.CharField(null=True,max_length=100)
    employeeId=models.CharField(null=True,max_length=100)
    date=models.DateField(null=True,)
    employeeTimeIn=models.TimeField(null=True,default=0)
    

class EmployeeTimeOut(models.Model):
    employeeName=models.CharField(null=True,max_length=100)
    employeeId=models.CharField(null=True,max_length=100)
    date=models.DateField(null=True,)
    employeeTimeOut=models.TimeField(null=True,default=0)
    employeeWorkDescription=models.TextField(null=True,)
    employeeStatus=models.CharField(max_length=50,default='present')

    
class EmpLeaveApplication(models.Model):
    employeeName=models.CharField(null=True,max_length=100)
    employeeId=models.CharField(null=True,max_length=100)
    date=models.DateField(null=True)
    reasonForLeave=models.TextField(null=True)
    employeeStatus=models.CharField(max_length=50,default='absent')

    
    
    