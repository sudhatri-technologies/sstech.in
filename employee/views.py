from django.shortcuts import render,redirect
from .forms import EmployeeTimeInForm,EmployeeTimeOutForm,EmpLeaveApplicationForm

from hrm_admin.models import Employee

# Create your views here.

def empDashboard(request):
    return render(request,'employee/dashboard.html')


def checkIn(request):
    # from accounts.views import current_employee
    # currentEmployee =Employee.objects.get(employeeId=current_employee)


    if request.method == 'POST':
        form = EmployeeTimeInForm(request.POST)
        
        if(form.is_valid()):
            
            form.save()
            return redirect('checkin')
       
    else:
        form=EmployeeTimeInForm()
        
    
    context={'form':form}
    return render(request,'employee/checkin.html',context)

 
    
def checkOut(request):
    if request.method == 'POST':
        form = EmployeeTimeOutForm(request.POST)
       
        if(form.is_valid()):
            form.save()
            return redirect('checkout')

            
    else:
        form=EmployeeTimeOutForm()
    context={'form':form}
    return render(request,'employee/checkout.html',context)

def applyLeave(request):
    if request.method == 'POST':
        form = EmpLeaveApplicationForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('applyleave')

            
    else:
        form=EmpLeaveApplicationForm()
    context={'form':form}
    return render(request,'employee/applyleave.html',context)
    


def leaveReport(request):
    from accounts.views import current_employee
    EmpAbsentList=EmpLeaveApplication.objects.filter(employeeId=current_employee).order_by('-date')
    print(EmpAbsentList,'absent list')

    context={'absentList':EmpAbsentList}
    return render(request,'employee/leave-report.html',context)

import datetime
from .models import *

def attendenceHistory(request):
    from accounts.views import current_employee

    if request.method =='POST':
        pass
    else:
        EmpTimeIns=EmployeeTimeIn.objects.filter(employeeId=current_employee).order_by('-date')
        EmpTimeOuts=EmployeeTimeOut.objects.filter(employeeId=current_employee).order_by('-date')
        inTime=EmployeeTimeIn.objects.filter(employeeId=current_employee).order_by('-date').values_list('employeeTimeIn',flat=True)
        outTime=EmployeeTimeOut.objects.filter(employeeId=current_employee).order_by('-date').values_list('employeeTimeOut',flat=True)
        workingHours=[]
        for (i,o) in zip(inTime,outTime):
            diff=datetime.timedelta(hours=(o.hour-i.hour),minutes=(o.minute-i.minute),seconds=(o.second-i.second))
            workingHours.append(diff)
        arr2=[ [eTimeIns,eTimeOuts,workingHours] for eTimeIns,eTimeOuts,workingHours in zip(EmpTimeIns,EmpTimeOuts,workingHours)]
        # print(arr2,'arr1 is ')
        # for eI,eO in arr2:
        #     print(eI.employeeName,'Name is')
        #     print(eO.employeeWorkDescription,'work is')
        #     print(eO.employeeTimeOut,'time out is')
        context={'arr2':arr2}
        return render(request,'employee/attendence-history.html',context)

        


