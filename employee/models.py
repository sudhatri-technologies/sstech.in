from django.db import models
from hrm_admin.models import *

# Create your models here.
class EmployeeTimeIn(models.Model):
    employeeName=models.CharField(null=True,max_length=100)
    employeeId=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    employeeTimeIn=models.TimeField(null=True,default=0)
    
    

class EmployeeTimeOut(models.Model):
    employeeName=models.CharField(null=True,max_length=100)
    employeeId=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    employeeTimeOut=models.TimeField(null=True,default=0)
    employeeWorkDescription=models.TextField(null=True)
    employeeStatus=models.CharField(max_length=50,default='present')
    

    
class EmpLeaveApplication(models.Model):
    employeeName=models.CharField(null=True,max_length=100)
    employeeId=models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    reasonForLeave=models.TextField(null=True)
    employeeStatus=models.CharField(max_length=50,default='absent')
    

    
    
    