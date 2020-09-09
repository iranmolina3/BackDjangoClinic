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

def create_consulta(request):
    if(request.method == "POST"):
#        print(request.POST)
        _motivo_consulta = request.POST.get('MOTIVO_CONSULTA')
        _historia = request.POST.get('HISTORIA')
        print(_motivo_consulta, _historia)
        _model_consulta = Consulta(MOTIVO_CONSULTA = _motivo_consulta,
                                   HISTORIA = _historia)
        _model_consulta.save()
        return redirect('dashboard')
    return render(request, 'Clinic/Consulta/create_consulta.html')

def read_consulta(request):
    consulta = Consulta.objects.filter(ESTADO = True)
    print(consulta)
    paginator = Paginator(consulta, 6)
    page = request.GET.get('page')
    consulta = paginator.get_page(page)
    return render(request, 'Clinic/Consulta/read_consulta.html', {'consulta':consulta})

def update_consulta(request, pk_consulta):
    consulta = Consulta.objects.get(PK_CONSULTA = pk_consulta)
    if(request.method == "GET"):
        return render(request, 'Clinic/Consulta/update_consulta.html', {'consulta': consulta})
    else:
        _motivo_consulta = request.POST.get('MOTIVO_CONSULTA')
        _historia = request.POST.get('HISTORIA')
        consulta.MOTIVO_CONSULTA = _motivo_consulta
        consulta.HISTORIA = _historia
        consulta.save()
        return redirect('dashboard')

def delete_consulta(request, pk_consulta):
    consulta = Consulta.objects.get(PK_CONSULTA = pk_consulta)
    if(request.method == "GET"):
        return render(request, 'Clinic/Consulta/delete_consulta.html', {'consulta':consulta})
    else:
        consulta.ESTADO = False
        consulta.save()
        return redirect('dashboard')

def create_examen_fisico(request):
    if(request.method == "POST"):
#        print(request.POST)
        _presion_arterial = request.POST.get('PRESION_ARTERIAL')
        _frecuencia_cardiaca = request.POST.get('FRECUENCIA_CARDIACA')
        _frecuencia_respiratoria = request.POST.get('FRECUENCIA_RESPIRATORIA')
        _temperatura = request.POST.get('TEMPERATURA')
        _frecuencia_cardiaca_fetal = request.POST.get('FRECUENCIA_CARDIACA_FETAL')
        _impresion_clinica = request.POST.get('IMPRESION_CLINCIA')
        print(_presion_arterial, _frecuencia_cardiaca, _frecuencia_respiratoria, _temperatura, _frecuencia_cardiaca_fetal, _impresion_clinica)
        _model_examen_fisico = ExamenFisico(PRESION_ARTERIAL = _presion_arterial, FRECUENCIA_CARDIACA = _frecuencia_cardiaca,
                                        FRECUENCIA_RESPIRATORIA = _frecuencia_respiratoria, TEMPERATURA = _temperatura,
                                        FRECUENCIA_CARDIACA_FETAL = _frecuencia_cardiaca_fetal, IMPRESION_CLINCIA = _impresion_clinica)
        _model_examen_fisico.save()
        return redirect('dashboard')
    return render(request, 'Clinic/ExamenFisico/create_examen_fisico.html')

def read_examen_fisico(request):
    examen_fisico = ExamenFisico.objects.filter(ESTADO = True)
    print(examen_fisico)
    paginator = Paginator(examen_fisico, 6)
    page = request.GET.get('page')
    examen_fisico = paginator.get_page(page)
    return render(request, 'Clinic/ExamenFisico/read_examen_fisico.html', {'examen_fisico':examen_fisico})

def update_examen_fisico(request, pk_examen_fisico):
    examen_fisico = ExamenFisico.objects.get(PK_EXAMEN_FISICO = pk_examen_fisico)

    var = examen_fisico.PRESION_ARTERIAL
    if(request.method == "GET"):
        return render(request, 'Clinic/ExamenFisico/update_examen_fisico.html', {'examen_fisico': examen_fisico, 'var': int(var)})
    else:
        _presion_arterial = request.POST.get('PRESION_ARTERIAL')
        _frecuencia_cardiaca = request.POST.get('FRECUENCIA_CARDIACA')
        _frecuencia_respiratoria = request.POST.get('FRECUENCIA_RESPIRATORIA')
        _temperatura = request.POST.get('TEMPERATURA')
        _frecuencia_cardiaca_fetal = request.POST.get('FRECUENCIA_CARDIACA_FETAL')
        _impresion_clinica = request.POST.get('IMPRESION_CLINCIA')
        examen_fisico.MOTIVO_CONSULTA = _presion_arterial
        examen_fisico.HISTORIA = _frecuencia_cardiaca
        examen_fisico.FRECUENCIA_RESPIRATORIA = _frecuencia_respiratoria
        examen_fisico.TEMPERATURA = _temperatura
        examen_fisico.FRECUENCIA_CARDIACA_FETAL = _frecuencia_cardiaca_fetal
        examen_fisico.IMPRESION_CLINCIA = _impresion_clinica
        examen_fisico.save()
        return redirect('dashboard')

def delete_examen_fisico(request, pk_examen_fisico):
    examen_fisico = ExamenFisico.objects.get(PK_EXAMEN_FISICO = pk_examen_fisico)
    print(examen_fisico)
    if(request.method == "GET"):
        return render(request, 'Clinic/ExamenFisico/delete_examen_fisico.html')
    else:
        examen_fisico.ESTADO = False
        examen_fisico.save()
        return redirect('dashboard')

def create_antecedente(request):
    if(request.method == "POST"):
#        print(request.POST)
        _ultima_regla = request.POST.get('ULTIMA_REGLA')
        _fecha_probable_parto = request.POST.get('FECHA_PROBABLE_PARTO')
        _gesta = request.POST.get('GESTA')
        _aborto = request.POST.get('ABORTO')
        _hijos_vivos = request.POST.get('HIJOS_VIVOS')
        _peso = request.POST.get('PESO')
        _quirurgico = request.POST.get('QUIRURGICO')
        _medico = request.POST.get('MEDICO')
        _alergia = request.POST.get('ALERGIA')
        _familiar = request.POST.get('FAMILIAR')
        _habito = request.POST.get('HABITO')
        _cigarro = request.POST.get('CIGARRO')
        _licor = request.POST.get('LICOR')
        print(_ultima_regla, _fecha_probable_parto, _gesta,
              _aborto, _hijos_vivos, _peso, _quirurgico, _medico, _alergia, _familiar, _habito,
              _cigarro, _licor)
        _model_antecedente = Antecedente(ULTIMA_REGLA = _ultima_regla, FECHA_PROBABLE_PARTO = _fecha_probable_parto,
                                        GESTA = _gesta, ABORTO = _aborto, HIJOS_VIVOS = _hijos_vivos,
                                        PESO = _peso, QUIRURGICO = _quirurgico, MEDICO = _medico, ALERGIA = _alergia,
                                        FAMILIAR = _familiar, HABITO = _habito, CIGARRO = _cigarro,
                                        LICOR = _licor)
        _model_antecedente.save()
        return redirect('dashboard')
    return render(request, 'Clinic/Antecedente/create_antecedente.html')

def read_antecedente(request):
    antecedente = Antecedente.objects.filter(ESTADO = True)
    print(antecedente)
    paginator = Paginator(antecedente, 6)
    page = request.GET.get('page')
    antecedente = paginator.get_page(page)
    return render(request, 'Clinic/ExamenFisico/read_examen_fisico.html', {'antecedente':antecedente})