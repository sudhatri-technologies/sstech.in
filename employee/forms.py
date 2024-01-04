from django import forms
from employee.models import EmployeeTimeIn,EmployeeTimeOut,EmpLeaveApplication

import datetime
date_time=datetime.datetime.now()
date=date_time.strftime("%Y-%m-%d")
time=date_time.strftime("%X")
context={
        'date':date
        }

from hrm_admin.models import Employee

class EmployeeTimeInForm(forms.ModelForm):
    
    class Meta:
        model=EmployeeTimeIn
        fields='__all__'
        labels={
            'employeeName':'Employee Name',
            'employeeTimeIn':'Time',
            'employeeId':'Employee Id'
        }
    
    
    def __init__(self,*args,**kwargs):            #add this
         super(EmployeeTimeInForm,self).__init__(*args,**kwargs)
         from accounts.views import current_employee
         currentEmployee =Employee.objects.get(employeeId=current_employee)

         self.fields['employeeName'].initial=currentEmployee.firstName
         self.fields['employeeId'].initial=currentEmployee.employeeId
         self.fields['date'].initial=date
         date_time=datetime.datetime.now()
         time=date_time.strftime("%X")
         self.fields['employeeTimeIn'].initial=time
         self.fields['date'].widget.attrs['readonly'] = True
         self.fields['employeeTimeIn'].widget.attrs['readonly'] = True
         #self.fields['employeeId'].widget.attrs['readonly'] = True
         #self.fields['employeeId'].widget.attrs['disabled'] = True


         self.fields['employeeId'].empty_label="select"


         
class EmployeeTimeOutForm(forms.ModelForm):
    class Meta:
        model=EmployeeTimeOut
        fields='__all__'
        labels={
            'employeeName':'Employee Name',
            'employeeTimeOut':'Time',
            'employeeId':'Employee Id',
            'employeeWorkDescription':'Work Description'
        }
    
    
    def __init__(self,*args,**kwargs):            #add this
         super(EmployeeTimeOutForm,self).__init__(*args,**kwargs)
         self.fields['employeeWorkDescription'].widget.attrs = {'rows': 5,'cols':50}
         from accounts.views import current_employee
         currentEmployee =Employee.objects.get(employeeId=current_employee)

         self.fields['employeeName'].initial=currentEmployee.firstName
         self.fields['employeeId'].initial=currentEmployee.employeeId
        

         self.fields['date'].initial=date
         date_time=datetime.datetime.now()
         time=date_time.strftime("%X")
         self.fields['employeeTimeOut'].initial=time
         self.fields['date'].widget.attrs['readonly'] = True
         self.fields['employeeTimeOut'].widget.attrs['readonly'] = True
         self.fields['employeeStatus'].required=False
         self.fields['employeeId'].empty_label="select"

         


class EmpLeaveApplicationForm(forms.ModelForm):
    class Meta:
        model=EmpLeaveApplication
        fields='__all__'
        labels={
            'employeeName':'Employee Name',
            'employeeId':'Employee Id',
            'reasonForLeave':'Reason For Leave'
        }
    
    
    def __init__(self,*args,**kwargs):            #add this
         super(EmpLeaveApplicationForm,self).__init__(*args,**kwargs)
         self.fields['reasonForLeave'].widget.attrs = {'rows': 5,'cols':50}
         from accounts.views import current_employee
         currentEmployee =Employee.objects.get(employeeId=current_employee)

         self.fields['employeeName'].initial=currentEmployee.firstName
         self.fields['employeeId'].initial=currentEmployee.employeeId
        
         
         self.fields['date'].initial=date
         self.fields['date'].widget.attrs['readonly'] = True
         self.fields['employeeStatus'].required=False
         self.fields['employeeId'].empty_label="select"


         









