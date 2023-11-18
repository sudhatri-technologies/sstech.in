from django.shortcuts import render,redirect
from .forms import EmployeeTimeInForm,EmployeeTimeOutForm,EmpLeaveApplicationForm


# Create your views here.
def checkIn(request):
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
    





