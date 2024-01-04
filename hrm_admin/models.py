from django.db import models

# Create your models here.
class Department(models.Model):
    deptName=models.CharField(max_length=64)
    def __str__(self):
        return self.deptName

class Position(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Employee(models.Model):
    firstName=models.CharField(max_length=64)
    lastName=models.CharField(max_length=64)
    fatherName=models.CharField(max_length=64)
    email=models.EmailField()
    dOB=models.DateField()
    phoneNumber=models.IntegerField(max_length=10)
    maritialStatus=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    localAddress=models.TextField()
    permanentAddress=models.TextField()
    employeeId=models.CharField(primary_key=True,max_length=9)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    designation=models.ForeignKey(Position,on_delete=models.CASCADE)
    shift=models.CharField(max_length=50)
    dOJ=models.DateField()
    isAdmin=models.BooleanField(default=False)
    userName=models.CharField(max_length=10)
    password=models.CharField(max_length=9)

    def __str__(self):
        return self.employeeId
