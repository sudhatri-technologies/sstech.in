from django.shortcuts import render,redirect
from accounts.forms import LoginForm
from hrm_admin.models import Employee
from employee.views import *
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
current_employee = None

def index(request):
    global current_employee
    if request.method =="POST":
        form=LoginForm(request.POST)
        if(form.is_valid()):
            user=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            userAdmin=Employee.objects.filter(employeeId=user,password=pwd,isAdmin=True)
            userEmp=Employee.objects.filter(employeeId=user,password=pwd,isAdmin=False)
            #currentEmployee =Employee.objects.get(employeeId=user)
            current_employee=user
            #print(current_employee)

            if userAdmin:
                return redirect('dashboard')
                

            elif userEmp:
                #current_employee=currentEmployee
                return redirect('empdashboard')
            else:
                messages.error(request,'invalid credentials')
                return redirect('index')
           
        
    else:
        form=LoginForm()
        context={'form':form}
        return render(request,'accounts/index.html',context)

def logout(request):
    
    return redirect('/')


from hrm import settings

from django.contrib import messages

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from .tokens import custom_token_generator




# PasswordReset - Request password reset form
def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = Employee.objects.filter(email=email).first()
        if user is not None:
            # Generate token and URL for password reset
            token = custom_token_generator.make_token(user)
            print('type and token from password reset request is',type(token),token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(f'/reset/{uid}/{token}/')
            #reset_link = request.build_absolute_uri('reset/' + uid + '/' + token + '/')

            protocol = 'http'
            token=token
            uid=uid
            domain = '127.0.0.1:8008/'
            print('reset is the below',reset_link)

            # Send reset link to the user's email
            subject = 'Password Reset Request'
            message = render_to_string('password_reset/password_reset_email.html', {
                'reset_link': reset_link,'protocol': 'https','domain': domain,'token':token,'uid':uid,'protocol':protocol
            })
            
           
            from_email=settings.EMAIL_HOST_USER
            to_list=[user.email]
            
            send_mail(subject, message,from_email,to_list,fail_silently=True)
            
            messages.success(request, 'Password reset email has been sent.')
            return redirect('password_reset_done')  # Redirect to a success page
        else:
            messages.error(request, 'No user associated with this email.')
    return render(request, 'password_reset/password_reset_request.html')

# PasswordResetDone - Display a success message after sending the reset email
def password_reset_done(request):
    return render(request, 'password_reset/password_reset_done.html')

# PasswordResetConfirm - Handle password reset confirmation
def password_reset_confirm(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = Employee.objects.filter(pk=uid).first()
    print('user and uid is',uid,user,token,'token type=',type(token))
    print('type and token from password reset confirm is',type(token),token)



    if user is not None and custom_token_generator.check_token(user, token):
        # Password reset confirmed, allow user to set a new password
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            #user.set_password(new_password)
            user.password=new_password
            user.save()
            messages.success(request, 'Password has been reset successfully.')
            return redirect('password_reset_complete')  # Redirect to password reset complete page
        return render(request, 'password_reset/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
    else:
        messages.error(request, 'Invalid reset link.')
        return redirect('password_reset')

        


# PasswordResetComplete - Display a success message after password reset completion
def password_reset_complete(request):
    return render(request, 'password_reset/password_reset_complete.html')


