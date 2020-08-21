from django.shortcuts import render

# Create your views here.

def Bienvenido(request):
    return render(request, 'Clinic/index.html')

def Sesion(request):
    return render(request, 'Clinic/login.html')