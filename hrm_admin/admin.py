from django.contrib import admin
from hrm_admin.models import *
# Register your models here.
#admin.site.register(Employee)
# admin.site.register(Position)
#admin.site.register(Department)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','firstName','lastName','department']

admin.site.register(Employee,EmployeeAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=['id','deptName']

admin.site.register(Department,DepartmentAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display=['id','title']
admin.site.register(Position,PositionAdmin)

#username harish
#password 12345