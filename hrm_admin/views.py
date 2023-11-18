from django.shortcuts import render,redirect
from .forms import EmployeeForm
from hrm_admin.models import Employee,Department,Position
from employee.models import EmployeeTimeIn,EmployeeTimeOut,EmpLeaveApplication

# Create your views here.


def dashboard(request):
    departments=Department.objects.all()
    totalEmployees=Employee.objects.all()
    presentCount=EmployeeTimeOut.objects.filter(employeeStatus='present').count()
    absentCount=EmpLeaveApplication.objects.filter(employeeStatus='absent').count()
   
    d=Department.objects.values_list('deptName',flat=True)
    deptCount=[]
    for q in range(1,departments.count()+1):
        s=Employee.objects.filter(department__id__icontains=q).count()
        deptCount.append(s)
        # print(deptCount,"dept Counts are")
    arr1=[ [d,dC] for d,dC in zip(d,deptCount)]
    # print(arr1,'values of arraqy 1 is ')
    # for a1,a2 in arr1:
    #     print(a1,'a1 is')
    #     print(a2,'a2 is')
    context={'totalDepartments':departments.count(),'totalEmployees':totalEmployees.count(),'arr1':arr1,'presentCount':presentCount,'absentCount':absentCount}
    return render(request,'hrmadmin/dashboard.html',context)
    
# def addUpdateEmployee(request,id=''):
#     if request.method == "POST":
#         form =EmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form=EmployeeForm()
#     else:
#         if id=='':                       #insert operation
#             form=EmployeeForm()
#         else:                            #update operation
#             employee=Employee.objects.get(employeeId=id)  #filtering based on primarykey
#             form=EmployeeForm(instance=employee)
#     return render(request,'hrmadmin/add-employee.html',{'form':form})

def addUpdateEmployee(request,id=0):
    if(request.method=="GET"):
        if(id==0):             #insert operation
            form=EmployeeForm()
        else:                  #update operation
            employee=Employee.objects.get(pk=id)  #filtering based on primarykey
            form=EmployeeForm(instance=employee)
        return render(request,'hrmadmin/add-employee.html',{'form':form})
        
    else:          #POST request
        if(id==0):    #insert operation
            form=EmployeeForm(request.POST)
        else:
            employee=Employee.objects.get(pk=id)  #filtering based on primarykey
            form=EmployeeForm(request.POST,instance=employee)
        if(form.is_valid()):
            form.save()
        return redirect('dashboard')



def manageEmployee(request):
    if request.method =='POST':
        pass
    else:
        employees=Employee.objects.all()
        context={'employees':employees}
        
        return render(request,'hrmadmin/manage-employee.html',context)
import datetime
def attendance(request):
    if request.method =='POST':
        pass
    else:
        EmpTimeIns=EmployeeTimeIn.objects.all()
        EmpTimeOuts=EmployeeTimeOut.objects.all()
        EmpAbsentList=EmpLeaveApplication.objects.all()
        inTime=EmployeeTimeIn.objects.values_list('employeeTimeIn',flat=True)
        outTime=EmployeeTimeOut.objects.values_list('employeeTimeOut',flat=True)
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
        context={'arr2':arr2,'absentList':EmpAbsentList}

        return render(request,'hrmadmin/attendance.html',context)



def deleteEmployee(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('manage')


