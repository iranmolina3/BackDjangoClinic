from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def create_persona(request):

    if(request.method == "POST"):
        print(request.POST)
        _nombre = request.POST.get('NOMBRE')
        _apellido = request.POST.get('APELLIDO')
        _dpi = request.POST.get('DPI')
        _genero = request.POST.get('GENERO')
        _edad = request.POST.get('EDAD')
        _fecha_nac = request.POST.get('FECHA_NACIMIENTO')
        _fk_estado_civil = request.POST.get('FK_ESTADO_CIVIL')
        _telefono = request.POST.get('TELEFONO')
        _direccion = request.POST.get('DIRECCION')
        _fk_municipio = request.POST.get('MUNICIPIO')
        municipio = Municipio.objects.get(PK_MUNICIPIO = _fk_municipio)
        estado_civil = EstadoCivil.objects.get(PK_ESTADO_CIVIL = _fk_estado_civil)
        print(_dpi, _edad, _genero, _nombre, _apellido, _direccion, _fecha_nac, _fk_estado_civil, estado_civil, municipio, _telefono)
        _model_persona = Persona(NOMBRE = _nombre,
                                 APELLIDO = _apellido,
                                 DPI = _dpi,
                                 EDAD = _edad,
                                 FECHA_NACIMIENTO = _fecha_nac,
                                 TELEFONO = _telefono,
                                 GENERO = _genero,
                                 DIRECCION = _direccion,
                                 FK_MUNICIPIO = municipio,
                                 FK_ESTADO_CIVIL = estado_civil)
        _model_persona.save()
        return redirect('dashboard')
    municipio = Municipio.objects.all()
    estado_civil = EstadoCivil.objects.all()
    return render(request, 'Clinic/Persona/create_persona.html', {'municipio':municipio, 'estado_civil':estado_civil})

def read_persona(request):
    persona = Persona.objects.filter(ESTADO = True)
    paginator = Paginator(persona, 6)
    page = request.GET.get('page')
    persona = paginator.get_page(page)
    return render(request, 'Clinic/Persona/read_persona.html', {'persona':persona})

def update_persona(request, pk_persona):
    persona = Persona.objects.get(PK_PERSONA = pk_persona)
    if(request.method == "GET"):
        municipio = Municipio.objects.filter(ESTADO=True)
        estado_civil = EstadoCivil.objects.filter(ESTADO=True)
        fecha = persona.FECHA_NACIMIENTO
        return render(request, 'Clinic/Persona/update_persona.html', {'persona': persona, 'estado_civil': estado_civil, 'municipio': municipio, 'fecha': str(fecha)})
    else:
        _nombre = request.POST.get('NOMBRE')
        _apellido = request.POST.get('APELLIDO')
        _dpi = request.POST.get('DPI')
        _genero = request.POST.get('GENERO')
        _edad = request.POST.get('EDAD')
        _fecha_nac = request.POST.get('FECHA_NACIMIENTO')
        _fk_estado_civil = request.POST.get('FK_ESTADO_CIVIL')
        _telefono = request.POST.get('TELEFONO')
        _direccion = request.POST.get('DIRECCION')
        _fk_municipio = request.POST.get('MUNICIPIO')
        municipio = Municipio.objects.get(PK_MUNICIPIO=_fk_municipio)
        estado_civil = EstadoCivil.objects.get(PK_ESTADO_CIVIL=_fk_estado_civil)
        persona.NOMBRE = _nombre
        persona.APELLIDO = _apellido
        persona.DPI = _dpi
        persona.GENERO = _genero
        persona.EDAD = _edad
        persona.FECHA_NACIMIENTO = _fecha_nac
        persona.TELEFONO = _telefono
        persona.DIRECCION = _direccion
        persona.FK_ESTADO_CIVIL = estado_civil
        persona.FK_MUNICIPIO = municipio
        persona.save()
        return redirect('dashboard')

def delete_persona(request, pk_persona):
    persona = Persona.objects.get(PK_PERSONA = pk_persona)
    if(request.method == "GET"):
        return render(request, 'Clinic/Persona/delete_persona.html', {'persona':persona})
    else:
        persona.ESTADO = False
        persona.save()
        return redirect('dashboard')
