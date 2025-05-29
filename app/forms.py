from django import forms
from .models import Employee,Leads

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password', 'phone', 'designation']

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.Select(attrs={"class":"form-select"})
        }


class LeadsForm(forms.ModelForm):
    class Meta:
        model = Leads  
        fields = ['name', 'email', 'phone', 'address', 'description', 'Priority', 'assigned_to','deadline']

        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control border border-2 shadow",'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={"class":"form-control border border-2 shadow",'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={"class":"form-control border border-2 shadow",'placeholder': 'Phone'}),
            'address': forms.TextInput(attrs={"class":"form-control border border-2 shadow",'placeholder': 'Address'}),
            'description': forms.Textarea(attrs={"class":"form-control border border-2 shadow",'placeholder': 'Description......',"rows":3}),
            'Priority': forms.Select(attrs={"class":"form-select border border-2 shadow"}),
            'assigned_to': forms.Select(attrs={"class":"form-select border border-2 shadow"}),
            'deadline': forms.DateTimeInput(attrs={"class":"form-control border border-2 shadow",'type': 'datetime-local'}),
        }

class Employee_login_Form(forms.Form):

    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder': 'Password'}))
    