from django.contrib import admin
from employee.models import EmployeeTimeIn,EmployeeTimeOut,EmpLeaveApplication
# Register your models here.
class EmployeeTimeInAdmin(admin.ModelAdmin):
    list_display=['id','employeeName','employeeId']
admin.site.register(EmployeeTimeIn,EmployeeTimeInAdmin)

class EmployeeTimeOutAdmin(admin.ModelAdmin):
    list_display=['id','employeeName','employeeId']
admin.site.register(EmployeeTimeOut,EmployeeTimeOutAdmin)

class EmpLeaveApplicationAdmin(admin.ModelAdmin):
    list_display=['id','employeeName','employeeId']
admin.site.register(EmpLeaveApplication,EmpLeaveApplicationAdmin)