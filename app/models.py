from django.db import models



class Employee(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=15)
    desigination_choice = (
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Telicaller', 'TeliCaller'),
        ("Admin", 'Admin'),
    )
    designation = models.CharField(max_length=50, choices=desigination_choice,default="Manager")

    def __str__(self):
        return self.username

class Leads(models.Model):
    Priority_choice = (
        ('Hot', 'Hot'),
        ('Warm', 'Warm'),
        ('Cold', 'Cold'),
    )
    status_choice = (
        ('Not Accepted', 'Not Accepted'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField() 
    Priority = models.CharField(max_length=50, choices=Priority_choice, default='Hot')
    status=models.CharField(max_length=50, choices=status_choice, default='Not Accepted')
    assigned_on = models.DateField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leads')  
