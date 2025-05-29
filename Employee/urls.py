"""
URL configuration for Employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.manager_login, name='manager_login'),
    path('manager/logout/', views.Manager_logout, name='manager_logout'),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('manager/create-employees/', views.manager_create_employees, name='manager_create_employees'),
    path('manager/edit-employee/<int:id>/', views.manager_edit_employee, name='manager_edit_employee'),
    path('manager/delete-employee/<int:id>/', views.manager_delete_employee, name='manager_delete_employee'),
    path('manager/create-leads/', views.manager_assign_lead, name='manager_create_leads'),
    path("manager/leads/list/",views.manager_leads_list,name="manager_leads_list"),

    # employeee================================
    path('employee/login/', views.Employee_login, name='employee_login'),
    path("employee/dashboard/", views.employee_dashboard, name='employee_dashboard'),
    path("employee/leads/", views.employee_leads_list, name='employee_leads'),
    path("employee/logout/", views.employee_logout, name='employee_logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
