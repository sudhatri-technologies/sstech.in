from django import  forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
            'password':forms.PasswordInput(),
            'dOB':forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'dOJ':forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}),
            'userName':forms.TextInput(attrs={'placeholder':'EmployeeID & Username be Same'}),

            
                 }
    def __init__(self,*args,**kwargs):            #add this
         super(EmployeeForm,self).__init__(*args,**kwargs)
         self.fields['department'].empty_label="select"
         self.fields['designation'].empty_label="select"
         self.fields['localAddress'].widget.attrs = {'rows': 3,'cols':22}
         self.fields['permanentAddress'].widget.attrs = {'rows': 3,'cols':22}
