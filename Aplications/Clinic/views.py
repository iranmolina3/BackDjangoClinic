from django.shortcuts import render, redirect
from .forms import *
# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def create_rol(request):
    if(request.method == 'POST'):
        _formRol = FormRol(request.POST)
        print(request.POST)
        if _formRol.is_valid():
            _formRol.save()
            return redirect('index')
    else:
        _formRol = FormRol()
    #print(_formRol)
    return render(request, 'Clinic/create_rol.html', {'formRol':_formRol})

