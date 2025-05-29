from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import EmployeeForm,Employee_login_Form,LeadsForm
from .models import Employee,Leads

def manager_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('manager_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user.is_superuser:
            login(request, user)
            return redirect('manager_dashboard')
        else:
            error_message = "Invalid credentials or insufficient privileges. Please try again."
            return render(request, 'manager_login.html', {'error': error_message})

    return render(request, 'manager_login.html')

def Manager_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('manager_login')



@login_required(login_url='manager_login')
def manager_dashboard(request):
    if request.user.is_superuser:
        employees_count=Employee.objects.count()
        total_leads=Leads.objects.count() 
        pending_leads=Leads.objects.filter(status__in=["Not Accepted"]).count()
        inprogress_leads=Leads.objects.filter(status__in=["In Progress"]).count()
        completed_leads=Leads.objects.filter(status__in=["Completed"]).count()

    context={
        "employee":employees_count,
        "total_leads":total_leads,
        "pending":pending_leads,
        "inprogress":inprogress_leads,
        "complete":completed_leads,
    }
    return render(request, 'manager_dashboard.html',context)



@login_required(login_url='manager_login')   
def manager_create_employees(request):
    list= Employee.objects.all()
    if request.method=="POST":
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    return render(request, 'manager_create_employees.html', {'form': form, 'list': list})


@login_required(login_url='manager_login')   
def manager_edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('manager_create_employees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'manager_edit_employee.html', {'form': form, 'employee': employee})


def manager_delete_employee(request,id):
    employee=Employee.objects.get(id=id)
    if request.method=="POST":
        employee.delete()
        return redirect('manager_create_employees')
    

@login_required(login_url='manager_login')   
def manager_assign_lead(request):
    if request.method == "POST":
        form = LeadsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_create_employees')
    else:
        form = LeadsForm()
    return render(request, 'manager_assign_lead.html', {'form': form})

def manager_leads_list(request):
    leads=Leads.objects.all()
    return render(request,"manager_leads_list.html",{"leads":leads})


# employee================================================================================


def Employee_login(request):
    if request.method=="POST":
        form=Employee_login_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                employee=Employee.objects.get(username=username,password=password)
                request.session['employee_id'] = employee.id
                return redirect('employee_dashboard')
            except Employee.DoesNotExist:
                error_message = "Invalid credentials. Please try again."
                return render(request, 'employee_login.html', {'form': form, 'error': error_message})
    else:
        form = Employee_login_Form()
    return render(request, 'employee_login.html', {'form': form})

def employee_dashboard(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('employee_login') 

    
    employee = Employee.objects.get(id=employee_id)
    total_leads=Leads.objects.filter(assigned_to=employee).count() 
    pending_leads=Leads.objects.filter(assigned_to=employee,status__in=["Not Accepted"]).count()
    inprogress_leads=Leads.objects.filter(assigned_to=employee,status__in=["In Progress"]).count()
    completed_leads=Leads.objects.filter(assigned_to=employee,status__in=["Completed"]).count()

    context= {
        'employee': employee,
        "total_leads": total_leads,
        "pending":pending_leads,
        "inprogress":inprogress_leads,
        "completed":completed_leads
        }
    return render(request, 'employee_dashboard.html',context)



def employee_leads_list(request):
    employee_id = request.session.get('employee_id')
    if not employee_id:
        return redirect('employee_login') 

    employee = Employee.objects.get(id=employee_id)

    if request.method == "POST":
        lead_id = request.POST.get("lead_id")
        new_status = request.POST.get("status")
        lead = get_object_or_404(Leads, id=lead_id, assigned_to=employee)
        if new_status in dict(Leads.status_choice).keys():
            lead.status = new_status
            lead.save()
            return redirect('employee_leads')

    leads = employee.leads.all()
    status_choices = Leads.status_choice  # ✅ added this
    return render(request, 'employee_leads_list.html', {
        'leads': leads,
        'employee': employee,
        'status_choices': status_choices,  # ✅ added this
    })



def employee_logout(request):
    if 'employee_id' in request.session:
        del request.session['employee_id']
    return redirect('employee_login')