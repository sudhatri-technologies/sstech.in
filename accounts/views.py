from django.shortcuts import render,redirect
from accounts.forms import LoginForm
from hrm_admin.models import Employee
from employee.views import *
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method =="POST":
        form=LoginForm(request.POST)
        if(form.is_valid()):
            user=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            userAdmin=Employee.objects.filter(userName=user,password=pwd,isAdmin=True)
            userEmp=Employee.objects.filter(userName=user,password=pwd,isAdmin=False)
            

            if userAdmin:
                return redirect('dashboard')
                

            elif userEmp:
                return redirect('checkin')
            else:
                messages.error(request,'invalid credentials')
                return redirect('index')
           
        
    else:
        form=LoginForm()
        context={'form':form}
        return render(request,'accounts/index.html',context)

def logout(request):
    
    return redirect('/')