from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def Home(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        form.save()
        form = EmployeeForm()

    data = Employee.objects.all()

    context = {
        'form': form,
        'data': data,
    }

    return render(request, 'app2/dashboard.html',context)

def Delete(request, id):
    a = Employee.objects.get(pk = id)
    a.delete()
    return redirect('home')

def Update(request, id):
    if request.method == 'POST':
        data = Employee.objects.get(pk = id)
        form  = EmployeeForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
    else:
        data = Employee.objects.get(pk = id)
        form  = EmployeeForm(instance = data)
    context = {
        'form': form
    }
    return render(request,'app2/update.html',context)
