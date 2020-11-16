from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import date, datetime
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.test import TestCase


"""
 -- GLOBAL VARS
"""


def logout_view(request):
    logout(request)
    return redirect('index')


def generator_password():
    #   generador de contrasenia
    longitud = 8
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _password = ""
    _password = _password.join([choice(valores) for i in range(longitud)])
    print("CONTRASENIA DE USUARIO ", _password)
    return _password


def generator_carnet(_nombre, contador):
    #   generador de usuario con contador if a same user
    year = date.today().strftime("%Y")
    usuario = Usuario.objects.filter(ESTADO=True, CARNET__regex=str(_nombre) + str(year))
    for lista_usuario in usuario:
        print(lista_usuario)
        contador = contador + 1
    _carnet = str(_nombre) + str(year) + str(contador)
    return _carnet


"""
 -- INDEX
"""


def home(request):
    model_servicio = Servicio.objects.filter(estado=True)
    model_control_clinica = ControlClinica.objects.filter(estado=True)[:1].get()
    _number_servicio = countModelarray(Servicio.objects.filter(estado=True))
    _number_servicio = countModelarray(Servicio.objects.filter(estado=True))
    _number_satisfacion = countModelarray(Nps.objects.filter(respuesta=5)) + countModelarray(
        Nps.objects.filter(respuesta=4)) + countModelarray(Nps.objects.filter(respuesta=3))
    model_historial_clinico = HistorialClinico.objects.all()[:10]
    return render(request, 'index.html',
                  {'model_control_clinica': model_control_clinica, 'model_servicio': model_servicio,
                   'number_servicio': _number_servicio, 'number_satisfacion': _number_satisfacion,
                   'model_historial_clinico': model_historial_clinico})


def servicios(request):
    model_servicio = Servicio.objects.filter(estado=True)
    model_control_clinica = ControlClinica.objects.filter(estado=True)[:1].get()
    _number_servicio = countModelarray(Servicio.objects.filter(estado=True))
    _number_servicio = countModelarray(Servicio.objects.filter(estado=True))
    _number_satisfacion = countModelarray(Nps.objects.filter(respuesta=5)) + countModelarray(
        Nps.objects.filter(respuesta=4)) + countModelarray(Nps.objects.filter(respuesta=3))
    model_historial_clinico = HistorialClinico.objects.all()[:10]
    return render(request, 'services.html',
                  {'model_control_clinica': model_control_clinica, 'model_servicio': model_servicio,
                   'number_servicio': _number_servicio, 'number_satisfacion': _number_satisfacion,
                   'model_historial_clinico': model_historial_clinico})


def contacto(request):
    model_servicio = Servicio.objects.filter(estado=True)
    model_control_clinica = ControlClinica.objects.filter(estado=True)[:1].get()
    _number_servicio = countModelarray(Servicio.objects.filter(estado=True))
    _number_servicio = countModelarray(Servicio.objects.filter(estado=True))
    _number_satisfacion = countModelarray(Nps.objects.filter(respuesta=5)) + countModelarray(
        Nps.objects.filter(respuesta=4)) + countModelarray(Nps.objects.filter(respuesta=3))
    model_historial_clinico = HistorialClinico.objects.all()[:10]
    return render(request, 'contact.html',
                  {'model_control_clinica': model_control_clinica, 'model_servicio': model_servicio,
                   'number_servicio': _number_servicio, 'number_satisfacion': _number_satisfacion,
                   'model_historial_clinico': model_historial_clinico})


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        _citas_atendidas = countModelarray(Cita.objects.filter(
            Q(tipo_estado=True) & Q(fecha=datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d"))))
        _citas_pendientes = countModelarray(Cita.objects.filter(
            Q(Q(estado=True) & Q(fecha=datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")))))
        _pacientes = countModelarray(Persona.objects.filter(estado=True))
        _citas_futuras = countModelarray(Cita.objects.filter(estado=True).exclude(
            fecha=datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")))
        # -- data stadistic Charts.js with Django - model Pacientes satisfechos
        _labels_nps = ['Muy malo', 'Malo', 'Normal', 'Bueno', 'Muy bueno']
        _label_nps = countModelarray(Nps.objects.filter(estado=True))
        _data_nps = []
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=1)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=2)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=3)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=4)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=5)))
        _label_servicio = labelModelservicio(Servicio.objects.filter(estado=True))
        _data_servicio = dataModelservicio(_label_servicio)

        _label_cita = ['Citas completadas', 'Citas canceladas']
        _data_cita = dataModelcita()

        _label_cita_date = labelModelcitadate(int(date.today().strftime("%m")))
        _data_cita_date = dataModelcitadate(int(date.today().strftime("%m")))

        # print(labelModelcitadate())
        return render(request, 'index_dashboard.html',
                      {'citas_atendidas': _citas_atendidas, 'citas_pendientes': _citas_pendientes,
                       'pacientes': _pacientes, 'citas_futuras': _citas_futuras, 'labels_nps': _labels_nps,
                       'label_nps': _label_nps, 'data_nps': _data_nps, 'label_servicio': _label_servicio,
                       'data_servicio': _data_servicio, 'data_cita': _data_cita, 'label_cita': _label_cita,
                       'label_cita_date': _label_cita_date, 'data_cita_date': _data_cita_date})


def dashboardFiltermonth(request, month):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        _citas_atendidas = countModelarray(Cita.objects.filter(
            Q(tipo_estado=True) & Q(fecha=datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d"))))
        _citas_pendientes = countModelarray(Cita.objects.filter(
            Q(Q(estado=True) & Q(fecha=datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")))))
        _pacientes = countModelarray(Persona.objects.filter(estado=True))
        _citas_futuras = countModelarray(Cita.objects.filter(estado=True).exclude(
            fecha=datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")))
        # -- data stadistic Charts.js with Django - model Pacientes satisfechos
        _labels_nps = ['Muy malo', 'Malo', 'Normal', 'Bueno', 'Muy bueno']
        _label_nps = countModelarray(Nps.objects.filter(estado=True))
        _data_nps = []
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=1)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=2)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=3)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=4)))
        _data_nps.append(countModelarray(Nps.objects.filter(respuesta=5)))
        _label_servicio = labelModelservicio(Servicio.objects.filter(estado=True))
        _data_servicio = dataModelservicio(_label_servicio)

        _label_cita = ['Citas completadas', 'Citas canceladas']
        _data_cita = dataModelcita()
        _label_cita_date = labelModelcitadate(month)
        _data_cita_date = dataModelcitadate(month)
        return render(request, 'index_dashboard.html',
                      {'citas_atendidas': _citas_atendidas, 'citas_pendientes': _citas_pendientes,
                       'pacientes': _pacientes, 'citas_futuras': _citas_futuras, 'labels_nps': _labels_nps,
                       'label_nps': _label_nps, 'data_nps': _data_nps, 'label_servicio': _label_servicio,
                       'data_servicio': _data_servicio, 'data_cita': _data_cita, 'label_cita': _label_cita,
                       'label_cita_date': _label_cita_date, 'data_cita_date': _data_cita_date})


def dataModelcitadate(month):
    _data = []
    _year = int(date.today().strftime("%Y"))
    _month = [1, 3, 5, 7, 8, 10, 12]
    if month in _month:
        for day in range(1, 32):
            count_cita = countModelarray(Cita.objects.filter(
                Q(tipo_estado=True) & Q(Q(fecha__year=_year) & Q(fecha__month=month) & Q(fecha__day=day))))
            # print(cita)
            _data.append(count_cita)
    elif month == 2:
        for day in range(1, 29):
            count_cita = countModelarray(Cita.objects.filter(
                Q(tipo_estado=True) & Q(Q(fecha__year=_year) & Q(fecha__month=month) & Q(fecha__day=day))))
            # print(cita)
            _data.append(count_cita)
    else:
        for day in range(1, 31):
            count_cita = countModelarray(Cita.objects.filter(
                Q(tipo_estado=True) & Q(Q(fecha__year=_year) & Q(fecha__month=month) & Q(fecha__day=day))))
            # print(cita)
            _data.append(count_cita)
    return (_data)


def labelModelcitadate(month):
    _label = []
    _year = int(date.today().strftime("%Y"))
    _month = [1, 3, 5, 7, 8, 10, 12]
    if month in _month:
        for day in range(1, 32):
            _date = str(_year) + "-" + str(month) + "-" + str(day)
            # print(type(_date), ' ', _date)
            # print(type(day), 'dia ', day)
            _label.append(_date)
    elif month == 2:
        for day in range(1, 29):
            _date = str(_year) + "-" + str(month) + "-" + str(day)
            # print(type(_date), ' ', _date)
            # print(type(day), 'dia ', day)
            _label.append(_date)
    else:
        for day in range(1, 31):
            _date = str(_year) + "-" + str(month) + "-" + str(day)
            # print(type(_date), ' ', _date)
            # print(type(day), 'dia ', day)
            _label.append(_date)
    return (_label)


def dataModelcita():
    data = []
    label = [True, False]
    for seq in range(len(label)):
        data.append(countModelarray(Cita.objects.filter(tipo_estado=label[seq])))
    return data


def dataModelservicio(label):
    data = []
    for seq in range(len(label)):
        data.append(countModelarray(Consulta.objects.filter(fk_servicio=Servicio.objects.get(nombre=label[seq]))))
    return data


def labelModelservicio(model):
    label = []
    for list_model in model:
        label.append(list_model.nombre)
    return label


def countModelarray(model):
    count = 0
    for list_model in model:
        count = count + 1
    return count


"""
 -- LOGIN
"""


def sing(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            pass
    return render(request, 'authentication-login1.html')


"""
 -- CRUD TO THE MODEL PERSONA 
"""


def create_persona(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
            _nombre = request.POST.get('nombre')
            _apellido = request.POST.get('apellido')
            _dpi = request.POST.get('dpi')
            _fecha_nacimiento = request.POST.get('fecha_nacimiento')
            _telefono = request.POST.get('telefono')
            _genero = request.POST.get('genero')
            _direccion = request.POST.get('direccion')
            _estado_civil = request.POST.get('estado_civil')
            _municipio = request.POST.get('municipio')
            _hora_inicio = request.POST.get('hora_inicio')
            fecha_nacimiento = datetime.strptime(_fecha_nacimiento, "%Y-%m-%d")
            fecha_actual = datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
            # print(type(_fecha_nacimiento))

            # strftime is a functions convert var type date to str
            # strptime is a functions convert var type str to date

            # -- process to calculate Edad
            # print(fecha_nacimiento.strftime("%Y"))
            # print(fecha_actual.strftime("%Y"))
            # -- remove int() to see the change type variable
            # print(type(int(fecha_nacimiento.strftime("%Y"))))
            # print(type(int(fecha_actual.strftime("%Y"))))
            _edad = int(fecha_actual.strftime("%Y")) - int(fecha_nacimiento.strftime("%Y"))
            # print('Mi edad es ', _edad)
            # print(_dpi, _edad, _genero, _nombre, _apellido, _direccion, _fecha_nacimiento, _estado_civil, _municipio,
            #      _telefono)
            print('HORA_INICIO', _hora_inicio)
            _hora_final = datetime.today().strftime("%Y-%m-%dT%H:%M")
            print('HORA_FINAL', _hora_final)
            model_persona = Persona(nombre=_nombre, apellido=_apellido, dpi=_dpi, edad=_edad,
                                    fecha_nacimiento=_fecha_nacimiento, telefono=_telefono, genero=_genero,
                                    direccion=_direccion, municipio=_municipio, estado_civil=_estado_civil,
                                    hora_inicio=_hora_inicio, hora_final=_hora_final)
            model_persona.save()
            return redirect('clinic:read_persona')
        else:
            _hora_inicio = datetime.today().strftime("%Y-%m-%dT%H:%M")
            print('HORA_INICIO', _hora_inicio)
            return render(request, 'Clinic/Persona/create_persona.html', {'hora_inicio':_hora_inicio})


def read_persona(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        nombre = request.GET.get('nombreapellido')
        # print(nombre)
        # print(type(nombre))
        datalist_persona = Persona.objects.filter(estado=True)
        if (nombre == None):
            model_persona = Persona.objects.filter(estado=True)
        else:
            model_persona = Persona.objects.filter(
                Q(estado=True) & Q(Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre)))
        # paginator = Paginator(persona, 6)
        # page = request.GET.get('page')
        # persona = paginator.get_page(page)
        return render(request, 'Clinic/Persona/read_persona.html',
                      {'datalist_persona': datalist_persona, 'model_persona': model_persona})


def update_persona(request, pk_persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_persona = Persona.objects.get(pk_persona=pk_persona)
        if (request.method == "GET"):

            # print(type(model_persona.fecha_nacimiento.strftime("%Y-%m-%d")))
            return render(request, 'Clinic/Persona/update_persona.html',
                          {'model_persona': model_persona,
                           'fecha_nacimiento': model_persona.fecha_nacimiento.strftime("%Y-%m-%d")})
        else:
            _nombre = request.POST.get('nombre')
            _apellido = request.POST.get('apellido')
            _dpi = request.POST.get('dpi')
            _fecha_nacimiento = request.POST.get('fecha_nacimiento')
            _telefono = request.POST.get('telefono')
            _genero = request.POST.get('genero')
            _direccion = request.POST.get('direccion')
            _estado_civil = request.POST.get('estado_civil')
            _municipio = request.POST.get('municipio')
            fecha_nacimiento = datetime.strptime(_fecha_nacimiento, "%Y-%m-%d")
            fecha_actual = datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
            _edad = int(fecha_actual.strftime("%Y")) - int(fecha_nacimiento.strftime("%Y"))
            model_persona.nombre = _nombre
            model_persona.apellido = _apellido
            model_persona.dpi = _dpi
            model_persona.genero = _genero
            model_persona.edad = _edad
            model_persona.fecha_nacimiento = _fecha_nacimiento
            model_persona.telefono = _telefono
            model_persona.direccion = _direccion
            model_persona.estado_civil = _estado_civil
            model_persona.municipio = _municipio
            model_persona.save()
            return redirect('clinic:read_persona')

def report_persona(request, pk_persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_persona = Persona.objects.get(pk_persona=pk_persona)
        return render(request, 'Clinic/Persona/report_persona.html',
                      {'model_persona': model_persona,
                       'fecha_nacimiento': model_persona.fecha_nacimiento.strftime("%Y-%m-%d")})


def updatePersona(request, pk_historial_clinico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
        model_persona = Persona.objects.get(pk_persona=model_historial_clinico.fk_persona.pk_persona)
        if (request.method == "GET"):

            # print(type(model_persona.fecha_nacimiento.strftime("%Y-%m-%d")))
            return render(request, 'Clinic/Persona/update_persona.html',
                          {'model_persona': model_persona,
                           'fecha_nacimiento': model_persona.fecha_nacimiento.strftime("%Y-%m-%d")})
        else:
            _nombre = request.POST.get('nombre')
            _apellido = request.POST.get('apellido')
            _dpi = request.POST.get('dpi')
            _fecha_nacimiento = request.POST.get('fecha_nacimiento')
            _telefono = request.POST.get('telefono')
            _genero = request.POST.get('genero')
            _direccion = request.POST.get('direccion')
            _estado_civil = request.POST.get('estado_civil')
            _municipio = request.POST.get('municipio')
            fecha_nacimiento = datetime.strptime(_fecha_nacimiento, "%Y-%m-%d")
            fecha_actual = datetime.strptime(date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
            _edad = int(fecha_actual.strftime("%Y")) - int(fecha_nacimiento.strftime("%Y"))
            model_persona.nombre = _nombre
            model_persona.apellido = _apellido
            model_persona.dpi = _dpi
            model_persona.genero = _genero
            model_persona.edad = _edad
            model_persona.fecha_nacimiento = _fecha_nacimiento
            model_persona.telefono = _telefono
            model_persona.direccion = _direccion
            model_persona.estado_civil = _estado_civil
            model_persona.municipio = _municipio
            model_persona.save()
            return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                            model_historial_clinico.fk_cita.pk_cita)


def delete_persona(request, pk_persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_persona = Persona.objects.get(pk_persona=pk_persona)
        model_persona.estado = False
        model_persona.save()
        return redirect('clinic:read_persona')


"""
 -- CRUD TO THE MODEL CITA
"""


def create_cita(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "GET"):
            nombre = request.GET.get('nombreapellido')
            # print(nombre)
            # print(type(nombre))
            datalist_persona = Persona.objects.filter(estado=True)
            if (nombre == None):
                model_persona = Persona.objects.filter(estado=True)
            else:
                model_persona = Persona.objects.filter(
                    Q(estado=True) & Q(Q(nombre__icontains=nombre) | Q(apellido__icontains=nombre)))
            # paginator = Paginator(persona, 6)
            # page = request.GET.get('page')
            # persona = paginator.get_page(page)
            return render(request, 'Clinic/Cita/create_cita.html',
                          {'datalist_persona': datalist_persona, 'model_persona': model_persona})
        else:
            _pk_persona = request.POST.get('pk_persona')
            print("id model persona ", _pk_persona)
            return redirect(reserve_cita(request, _pk_persona))


def reserve_cita(request, pk_persona):
    model_persona = Persona.objects.get(pk_persona=pk_persona)
    _fecha = request.POST.get('fecha')
    _numero = numero_cita(_fecha)
    model_cita = Cita(numero=_numero, fecha=_fecha, fk_persona=model_persona)
    model_cita.save()
    return 'clinic:read_cita'


def numero_cita(fecha):
    model_cita = Cita.objects.filter(fecha=fecha)
    contador = 1
    for lista_cita in model_cita:
        contador = contador + 1
    return contador


def read_cita(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "GET"):
            _fecha = request.GET.get('fecha')
            # print(_fecha)
            # print("TIPO DE VALOR ", type(_fecha))
            if (_fecha is None):
                model_cita = Cita.objects.filter(estado=True)
                return render(request, 'Clinic/Cita/read_cita.html', {'model_cita': model_cita})
            else:
                model_cita = Cita.objects.filter(Q(estado=True) & Q(fecha=_fecha))
                return render(request, 'Clinic/Cita/read_cita.html', {'model_cita': model_cita})
        else:
            return redirect(update_cita(request))


def delete_cita(request, pk_cita):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_cita = Cita.objects.get(pk_cita=pk_cita)
        model_cita.estado = False
        model_cita.tipo_estado = False
        model_cita.save()
        return redirect('clinic:read_cita')


def update_cita(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == "GET":
            return 'clinic:read_cita'
        else:
            _pk_cita = request.POST.get('pk_cita')
            _fk_persona = request.POST.get('fk_persona')
            model_cita = Cita.objects.get(pk_cita=_pk_cita)
            model_cita.estado = False
            model_cita.tipo_estado = False
            model_cita.save()
            return reserve_cita(request, _fk_persona)


"""
 -- CRUD TO THE MODEL HISTORIAL CLINICO
"""


def create_historial_clinico(request, pk_persona, pk_cita):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.filter(estado=True)
        if request.method == "GET":
            try:
                model_persona = Persona.objects.get(pk_persona=pk_persona)
                model_historial_clinico = HistorialClinico.objects.get(Q(estado=True) & Q(fk_persona=model_persona))
                # print("PACIENTE ", model_persona)                              #PACIENTE  8,edson franzua,andres gomez
                # print("CONSULTA ", model_historial_clinico.fk_consulta)        #CONSULTA None
                # print("TIPO ",type(model_historial_clinico.fk_consulta))       #TIPO <class 'NoneType'>
                print("ENTRO EN EL TRY")
                return render(request, 'Clinic/HistorialClinico/create_historial_clinico.html',
                              {'model_historial_clinico': model_historial_clinico, 'model_pregunta': model_pregunta})
            except ObjectDoesNotExist:
                _hora_inicio = datetime.strptime(datetime.today().strftime("%Y-%m-%dT%H:%M"), "%Y-%m-%dT%H:%M")
                # print("FECHA ACTUAL ", fecha_inicio)
                model_cita = Cita.objects.get(pk_cita=pk_cita)
                model_persona = Persona.objects.get(pk_persona=pk_persona)
                _nombre = model_persona.nombre + " " + model_persona.apellido
                model_historial_clinico = HistorialClinico(nombre=_nombre, fk_persona=model_persona, fk_cita=model_cita,
                                                           hora_inicio=_hora_inicio)
                model_historial_clinico.save()
                # print(model_historial_clinico.pk_historial_clinico)
                # print(model_persona)
                return render(request, 'Clinic/HistorialClinico/create_historial_clinico.html',
                              {'model_historial_clinico': model_historial_clinico, 'model_pregunta': model_pregunta})
        else:
            _pk_pregunta = request.POST.get('pk_pregunta')
            _respuesta = int(request.POST.get('respuesta'))
            # print(type(_pk_pregunta), ' ', _pk_pregunta)
            # print(type(_respuesta), ' ', _respuesta)
            model_persona = Persona.objects.get(pk_persona=pk_persona)
            model_historial_clinico = HistorialClinico.objects.get(Q(estado=True) & Q(fk_persona=model_persona))
            model_pregunta = Pregunta.objects.get(pk_pregunta=_pk_pregunta)
            if model_historial_clinico.fk_nps is None:
                model_nps = Nps(respuesta=_respuesta, fk_pregunta=model_pregunta)
                model_nps.save()
            else:
                model_nps = Nps.objects.get(pk_nps=model_historial_clinico.fk_nps.pk_nps)
                model_nps.respuesta = _respuesta
                model_nps.fk_pregunta = model_pregunta
                model_nps.save()
            model_historial_clinico.fk_nps = model_nps
            model_historial_clinico.save()
            return redirect('clinic:create_historial_clinico', pk_persona, pk_cita)


def read_historial_clinico(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        _nombre = request.GET.get('nombre')
        # model_historial_clinico = HistorialClinico.objects.all().order_by('-fecha_creacion')
        model_historial_clinico = HistorialClinico.objects.all().order_by('-fecha_creacion')
        model_pregunta = Pregunta.objects.filter(estado=True)
        if _nombre:
            model_historial_clinico = HistorialClinico.objects.filter(Q(nombre__icontains=_nombre)).order_by(
                '-fecha_creacion')
        # paginator = Paginator(historial_clinico, 3)
        # page = request.GET.get('page')
        # historial_clinico = paginator.get_page(page)
        return render(request, 'Clinic/HistorialClinico/read_historial_clinico.html',
                      {'model_historial_clinico': model_historial_clinico, 'model_pregunta': model_pregunta})

def read_historial_clinico(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        _nombre = request.GET.get('nombre')
        # model_historial_clinico = HistorialClinico.objects.all().order_by('-fecha_creacion')
        model_historial_clinico = HistorialClinico.objects.all().order_by('-fecha_creacion')
        model_pregunta = Pregunta.objects.filter(estado=True)
        if _nombre:
            model_historial_clinico = HistorialClinico.objects.filter(Q(nombre__icontains=_nombre)).order_by(
                '-fecha_creacion')
        # paginator = Paginator(historial_clinico, 3)
        # page = request.GET.get('page')
        # historial_clinico = paginator.get_page(page)
        return render(request, 'Clinic/HistorialClinico/read_historial_clinico.html',
                      {'model_historial_clinico': model_historial_clinico, 'model_pregunta': model_pregunta})

def delete_historial_clinico(request, pk_historial_clinico, pk_cita):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        _hora_final = datetime.strptime(datetime.today().strftime("%Y-%m-%dT%H:%M"), "%Y-%m-%dT%H:%M")
        _model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
        _model_historial_clinico.estado = False
        _model_historial_clinico.hora_final = _hora_final
        _model_historial_clinico.save()
        _model_cita = Cita.objects.get(pk_cita=pk_cita)
        _model_cita.estado = False
        _model_cita.tipo_estado = True
        _model_cita.save()
        return redirect('clinic:read_cita')


"""
 -- CRUD TO THE MODEL CONSULTA
"""


def create_consulta(request, pk_historial_clinico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.filter(estado=True)
        model_servicio = Servicio.objects.filter(estado=True)
        model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
        if request.method == "POST":
            _pk_servicio = request.POST.get('pk_servicio')
            model_servicio = Servicio.objects.get(pk_servicio=_pk_servicio)
            _historia = request.POST.get('historia')
            model_consulta = Consulta(fk_servicio=model_servicio, historia=_historia)
            model_consulta.save()
            model_historial_clinico.fk_consulta = model_consulta
            model_historial_clinico.save()
            return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                            model_historial_clinico.fk_cita.pk_cita)
        else:
            model_consulta = Consulta.objects.filter(estado=True)
            return render(request, 'Clinic/Consulta/create_consulta.html',
                          {'model_consulta': model_consulta, 'model_servicio': model_servicio})


def update_consulta(request, pk_consulta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.filter(estado=True)
        model_consulta = Consulta.objects.get(pk_consulta=pk_consulta)
        model_servicio = Servicio.objects.filter(estado=True)
        if request.method == "GET":
            return render(request, 'Clinic/Consulta/update_consulta.html',
                          {'model_consulta': model_consulta, 'model_servicio': model_servicio})
        else:
            model_historial_clinico = HistorialClinico.objects.get(fk_consulta=model_consulta)
            _pk_servicio = request.POST.get('pk_servicio')
            _historia = request.POST.get('historia')
            model_servicio = Servicio.objects.get(pk_servicio=_pk_servicio)
            model_consulta.fk_servicio = model_servicio
            model_consulta.historia = _historia
            model_consulta.save()
            return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                            model_historial_clinico.fk_cita.pk_cita)

def report_consulta(request, pk_consulta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_consulta = Consulta.objects.get(pk_consulta=pk_consulta)
        model_servicio = Servicio.objects.filter(estado=True)
        return render(request, 'Clinic/Consulta/report_consulta.html',
                      {'model_consulta': model_consulta, 'model_servicio': model_servicio})


def delete_consulta(request, pk_consulta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        consulta = Consulta.objects.get(PK_CONSULTA=pk_consulta)
        if (request.method == "GET"):
            return render(request, 'Clinic/Consulta/delete_consulta.html', {'consulta': consulta})
        else:
            consulta.ESTADO = False
            consulta.save()
            return redirect('dashboard')


def read_consulta(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        consulta = Consulta.objects.filter(ESTADO=True)
        print(consulta)
        paginator = Paginator(consulta, 6)
        page = request.GET.get('page')
        consulta = paginator.get_page(page)
        return render(request, 'Clinic/Consulta/report_consulta.html', {'consulta': consulta})


"""
 -- CRUD TO THE MODEL ANTECEDENTE
"""


def create_antecedente(request, pk_historial_clinico, tipo_antecedente):
    print("tipo ", type(tipo_antecedente))
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
        if request.method == "POST":
            if tipo_antecedente == 1:
                _ultima_regla = isBlank(request.POST.get('ultima_regla'))
                _fecha_probable_parto = isBlank(request.POST.get('fecha_probable_parto'))
                _gesta = isBlank(request.POST.get('gesta'))
                _aborto = isBlank(request.POST.get('aborto'))
                print(type(_ultima_regla), ' ', _ultima_regla)
                print(type(_fecha_probable_parto), ' ', _fecha_probable_parto)
                print(type(_gesta), ' ', _gesta)
                print(type(_aborto), ' ', _aborto)
                _hijos_vivos = int(request.POST.get('hijos_vivos'))
                print(type(_hijos_vivos), ' ', _hijos_vivos)
                _peso = request.POST.get('peso')
                _quirurgicos = request.POST.get('quirurgicos')
                _medicos = request.POST.get('medicos')
                _alergias = request.POST.get('alergias')
                _familiares = request.POST.get('familiares')
                _habitos = request.POST.get('habitos')
                _cigarrillos = request.POST.get('cigarrillos')
                _licor = request.POST.get('licor')
                model_antecedente = Antecedente(ultima_regla=_ultima_regla, fecha_probable_parto=_fecha_probable_parto,
                                                gesta=_gesta, aborto=_aborto, hijos_vivos=_hijos_vivos, peso=_peso,
                                                quirurgico=_quirurgicos, medico=_medicos, alergia=_alergias,
                                                familiar=_familiares, habito=_habitos, cigarro=_cigarrillos,
                                                licor=_licor, tipo_antecedente=tipo_antecedente)
                model_antecedente.save()
                model_historial_clinico.fk_antecedente = model_antecedente
                model_historial_clinico.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)
            else:
                _hijos_vivos = int(request.POST.get('hijos_vivos'))
                print(type(_hijos_vivos), ' ', _hijos_vivos)
                _peso = request.POST.get('peso')
                _quirurgicos = request.POST.get('quirurgicos')
                _medicos = request.POST.get('medicos')
                _alergias = request.POST.get('alergias')
                _familiares = request.POST.get('familiares')
                _habitos = request.POST.get('habitos')
                _cigarrillos = request.POST.get('cigarrillos')
                _licor = request.POST.get('licor')
                model_antecedente = Antecedente(hijos_vivos=_hijos_vivos, peso=_peso,
                                                quirurgico=_quirurgicos, medico=_medicos, alergia=_alergias,
                                                familiar=_familiares, habito=_habitos, cigarro=_cigarrillos,
                                                licor=_licor, tipo_antecedente=tipo_antecedente)
                model_antecedente.save()
                model_historial_clinico.fk_antecedente = model_antecedente
                model_historial_clinico.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)
        else:
            return render(request, 'Clinic/Antecedente/create_antecedente.html', {'tipo_antecedente': tipo_antecedente})


def isBlank(myString):
    if not (myString and myString.strip()):
        return None
    else:
        return myString


def isStr(myString):
    if not (myString and myString.strip()):
        return ""
    else:
        return myString


def isNone(myDate):
    print(type(myDate), ' -valor- ', myDate)
    if myDate is None:
        return ""
    else:
        print(type(myDate.strftime("%Y-%m-%dT%H:%M")), ' -valor- ', myDate.strftime("%Y-%m-%dT%H:%M"))
        return myDate.strftime("%Y-%m-%dT%H:%M")


def update_antecedente(request, pk_antecedente, tipo_antecedente):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.filter(estado=True)
        model_antecedente = Antecedente.objects.get(pk_antecedente=pk_antecedente)
        ultima_regla = isNone(model_antecedente.ultima_regla)
        fecha_probable_parto = isNone(model_antecedente.fecha_probable_parto)
        gesta = isNone(model_antecedente.gesta)
        aborto = isNone(model_antecedente.aborto)
        if request.method == "GET":
            return render(request, 'Clinic/Antecedente/update_antecedente.html',
                          {'model_antecedente': model_antecedente, 'tipo_antecedente': tipo_antecedente,
                           'ultima_regla': ultima_regla, 'fecha_probable_parto': fecha_probable_parto, 'gesta': gesta,
                           'aborto': aborto})
        else:
            model_historial_clinico = HistorialClinico.objects.get(fk_antecedente=model_antecedente)
            if tipo_antecedente == 1:
                _ultima_regla = isBlank(request.POST.get('ultima_regla'))
                _fecha_probable_parto = isBlank(request.POST.get('fecha_probable_parto'))
                _gesta = isBlank(request.POST.get('gesta'))
                _aborto = isBlank(request.POST.get('aborto'))
                _hijos_vivos = request.POST.get('hijos_vivos')
                _peso = request.POST.get('peso')
                _quirurgicos = request.POST.get('quirurgicos')
                _medicos = request.POST.get('medicos')
                _alergias = request.POST.get('alergias')
                _familiares = request.POST.get('familiares')
                _habitos = request.POST.get('habitos')
                _cigarrillos = request.POST.get('cigarrillos')
                _licor = request.POST.get('licor')
                model_antecedente.ultima_regla = _ultima_regla
                model_antecedente.fecha_probable_parto = _fecha_probable_parto
                model_antecedente.gesta = _gesta
                model_antecedente.aborto = _aborto
                model_antecedente.hijos_vivos = _hijos_vivos
                model_antecedente.peso = _peso
                model_antecedente.quirurgico = _quirurgicos
                model_antecedente.medico = _medicos
                model_antecedente.alergia = _alergias
                model_antecedente.familiar = _familiares
                model_antecedente.habito = _habitos
                model_antecedente.cigarro = _cigarrillos
                model_antecedente.licor = _licor
                model_antecedente.tipo_antecedente = tipo_antecedente
                model_antecedente.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)
            else:
                _hijos_vivos = request.POST.get('hijos_vivos')
                _peso = request.POST.get('peso')
                _quirurgicos = request.POST.get('quirurgicos')
                _medicos = request.POST.get('medicos')
                _alergias = request.POST.get('alergias')
                _familiares = request.POST.get('familiares')
                _habitos = request.POST.get('habitos')
                _cigarrillos = request.POST.get('cigarrillos')
                _licor = request.POST.get('licor')
                model_antecedente.hijos_vivos = _hijos_vivos
                model_antecedente.peso = _peso
                model_antecedente.quirurgico = _quirurgicos
                model_antecedente.medico = _medicos
                model_antecedente.alergia = _alergias
                model_antecedente.familiar = _familiares
                model_antecedente.habito = _habitos
                model_antecedente.cigarro = _cigarrillos
                model_antecedente.licor = _licor
                model_antecedente.tipo_antecedente = tipo_antecedente
                model_antecedente.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)

def report_antecedente(request, pk_antecedente, tipo_antecedente):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_antecedente = Antecedente.objects.get(pk_antecedente=pk_antecedente)
        ultima_regla = isNone(model_antecedente.ultima_regla)
        fecha_probable_parto = isNone(model_antecedente.fecha_probable_parto)
        gesta = isNone(model_antecedente.gesta)
        aborto = isNone(model_antecedente.aborto)
        return render(request, 'Clinic/Antecedente/report_antecedente.html',
                      {'model_antecedente': model_antecedente, 'tipo_antecedente': tipo_antecedente,
                       'ultima_regla': ultima_regla, 'fecha_probable_parto': fecha_probable_parto, 'gesta': gesta,
                       'aborto': aborto})


def read_antecedente(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        antecedente = Antecedente.objects.filter(ESTADO=True)
        paginator = Paginator(antecedente, 6)
        page = request.GET.get('page')
        antecedente = paginator.get_page(page)
        return render(request, 'Clinic/Antecedente/report_antecedente.html', {'antecedente': antecedente})


def delete_antecedente(request, pk_antecedente):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        antecedente = Antecedente.objects.get(PK_ANTECEDENTE=pk_antecedente)
        print(antecedente)
        if (request.method == "GET"):
            return render(request, 'Clinic/Antecedente/delete_antecedente.html')
        else:
            antecedente.ESTADO = False
            antecedente.save()
            return redirect('dashboard')


"""
 -- CRUD TO THE MODEL EXAMEN FISICO
"""


def create_examen_fisico(request, pk_historial_clinico, tipo_examen_fisico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == "POST":
            model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
            if tipo_examen_fisico == 1:
                _presion_arterial = int(request.POST.get('presion_arterial'))
                _frecuencia_cardiaca = int(request.POST.get('frecuencia_cardiaca'))
                _frecuencia_respitaroria = int(request.POST.get('frecuencia_respitaroria'))
                _temperatura = int(request.POST.get('temperatura'))
                _frecuencia_cardiaca_fetal = int(request.POST.get('frecuencia_cardiaca_fetal'))
                _impresion_clinica = request.POST.get('impresion_clinica')
                model_examen_fisico = ExamenFisico(presion_arterial=_presion_arterial,
                                                   frecuencia_cardiaca=_frecuencia_cardiaca,
                                                   frecuencia_respitaroria=_frecuencia_respitaroria,
                                                   temperatura=_temperatura,
                                                   frecuencia_cardiaca_fetal=_frecuencia_cardiaca_fetal,
                                                   impresion_clinica=_impresion_clinica,
                                                   tipo_examen_fisico=tipo_examen_fisico)
                model_examen_fisico.save()
                model_historial_clinico.fk_examen_fisico = model_examen_fisico
                model_historial_clinico.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)
            else:
                _presion_arterial = int(request.POST.get('presion_arterial'))
                _frecuencia_cardiaca = int(request.POST.get('frecuencia_cardiaca'))
                _frecuencia_respitaroria = int(request.POST.get('frecuencia_respitaroria'))
                _temperatura = int(request.POST.get('temperatura'))
                _impresion_clinica = request.POST.get('impresion_clinica')
                model_examen_fisico = ExamenFisico(presion_arterial=_presion_arterial,
                                                   frecuencia_cardiaca=_frecuencia_cardiaca,
                                                   frecuencia_respitaroria=_frecuencia_respitaroria,
                                                   temperatura=_temperatura,
                                                   impresion_clinica=_impresion_clinica,
                                                   tipo_examen_fisico=tipo_examen_fisico)
                model_examen_fisico.save()
                model_historial_clinico.fk_examen_fisico = model_examen_fisico
                model_historial_clinico.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)
        else:
            return render(request, 'Clinic/ExamenFisico/create_examen_fisico.html',
                          {'tipo_examen_fisico': tipo_examen_fisico})


def update_examen_fisico(request, pk_examen_fisico, tipo_examen_fisico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.filter(estado=True)
        model_examen_fisico = ExamenFisico.objects.get(pk_examen_fisico=pk_examen_fisico)
        if request.method == "GET":
            return render(request, 'Clinic/ExamenFisico/update_examen_fisico.html',
                          {'model_examen_fisico': model_examen_fisico, 'tipo_examen_fisico': tipo_examen_fisico})
        else:
            model_historial_clinico = HistorialClinico.objects.get(fk_examen_fisico=model_examen_fisico)
            if tipo_examen_fisico == 1:
                _presion_arterial = int(request.POST.get('presion_arterial'))
                _frecuencia_cardiaca = int(request.POST.get('frecuencia_cardiaca'))
                _frecuencia_respitaroria = int(request.POST.get('frecuencia_respitaroria'))
                _temperatura = int(request.POST.get('temperatura'))
                _frecuencia_cardiaca_fetal = int(request.POST.get('frecuencia_cardiaca_fetal'))
                _impresion_clinica = request.POST.get('impresion_clinica')
                model_examen_fisico.presion_arterial = _presion_arterial
                model_examen_fisico.frecuencia_cardiaca = _frecuencia_cardiaca
                model_examen_fisico.frecuencia_respitaroria = _frecuencia_respitaroria
                model_examen_fisico.temperatura = _temperatura
                model_examen_fisico.frecuencia_cardiaca_fetal = _frecuencia_cardiaca_fetal
                model_examen_fisico.impresion_clinica = _impresion_clinica
                model_examen_fisico.tipo_examen_fisico = tipo_examen_fisico
                model_examen_fisico.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)
            else:
                _hijos_vivos = request.POST.get('hijos_vivos')
                _peso = request.POST.get('peso')
                _quirurgicos = request.POST.get('quirurgicos')
                _medicos = request.POST.get('medicos')
                _alergias = request.POST.get('alergias')
                _familiares = request.POST.get('familiares')
                _habitos = request.POST.get('habitos')
                _cigarrillos = request.POST.get('cigarrillos')
                _licor = request.POST.get('licor')
                model_examen_fisico.hijos_vivos = _hijos_vivos
                model_examen_fisico.peso = _peso
                model_examen_fisico.quirurgico = _quirurgicos
                model_examen_fisico.medico = _medicos
                model_examen_fisico.alergia = _alergias
                model_examen_fisico.familiar = _familiares
                model_examen_fisico.habito = _habitos
                model_examen_fisico.cigarro = _cigarrillos
                model_examen_fisico.licor = _licor
                model_examen_fisico.tipo_examen_fisico = tipo_examen_fisico
                model_examen_fisico.save()
                return redirect('clinic:create_historial_clinico', model_historial_clinico.fk_persona.pk_persona,
                                model_historial_clinico.fk_cita.pk_cita)

def report_examen_fisico(request, pk_examen_fisico, tipo_examen_fisico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_examen_fisico = ExamenFisico.objects.get(pk_examen_fisico=pk_examen_fisico)
        return render(request, 'Clinic/ExamenFisico/report_examen_fisico.html',
                      {'model_examen_fisico': model_examen_fisico, 'tipo_examen_fisico': tipo_examen_fisico})


def delete_examen_fisico(request, pk_examen_fisico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        examen_fisico = ExamenFisico.objects.get(PK_EXAMEN_FISICO=pk_examen_fisico)
        print(examen_fisico)
        if (request.method == "GET"):
            return render(request, 'Clinic/ExamenFisico/delete_examen_fisico.html')
        else:
            examen_fisico.ESTADO = False
            examen_fisico.save()
            return redirect('dashboard')


"""
 -- CRUD TO THE MODEL MEDICAMENTO
"""


def create_medicamento(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == "POST":
            _nombre = request.POST.get('descripcion')
            if Medicamento.objects.filter(Q(nombre__icontains=_nombre) & Q(estado=True)).exists():
                estado_text_helper = True
                return render(request, 'Clinic/Medicamento/create_medicamento.html',
                              {'estado_text_helper': estado_text_helper})
            else:
                model_medicamento = Medicamento(nombre=_nombre)
                model_medicamento.save()
                model_medicamento = Medicamento.objects.filter(estado=True)
                return render(request, 'Clinic/Medicamento/read_medicamento.html',
                              {'model_medicamento': model_medicamento})
        else:
            estado_text_helper = False
            return render(request, 'Clinic/Medicamento/create_medicamento.html',
                          {'estado_text_helper': estado_text_helper})


def read_medicamento(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        _nombre = isStr(request.GET.get('nombre'))
        model_medicamento = Medicamento.objects.filter(Q(estado=True) & Q(nombre__icontains=_nombre))
        return render(request, 'Clinic/Medicamento/read_medicamento.html', {'model_medicamento': model_medicamento})


def update_medicamento(request, pk_medicamento):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_medicamento = Medicamento.objects.get(pk_medicamento=pk_medicamento)
        if request.method == "POST":
            _nombre = request.POST.get('descripcion')
            if Medicamento.objects.filter(Q(nombre__icontains=_nombre) & Q(estado=True)).exists():
                estado_text_helper = True
                return render(request, 'Clinic/Medicamento/update_medicamento.html',
                              {'estado_text_helper': estado_text_helper})
            else:
                model_medicamento.nombre = _nombre
                model_medicamento.save()
                model_medicamento = Medicamento.objects.filter(estado=True)
                return render(request, 'Clinic/Medicamento/read_medicamento.html',
                              {'model_medicamento': model_medicamento})
        else:
            estado_text_helper = False
            return render(request, 'Clinic/Medicamento/update_medicamento.html',
                          {'estado_text_helper': estado_text_helper, 'model_medicamento': model_medicamento})


def delete_medicamento(request, pk_medicamento):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_medicamento = Medicamento.objects.get(pk_medicamento=pk_medicamento)
        model_medicamento.estado = False
        model_medicamento.save()
        return redirect('clinic:read_medicamento')


"""
 -- CRUD TO THE MODEL RECETA
"""


def create_receta(request, pk_historial_clinico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
        if request.method == "POST":
            _nombre = request.POST.get('nombre')
            _recomendacion = request.POST.get('recomendacion')
            if Medicamento.objects.filter(Q(nombre__icontains=_nombre) & Q(estado=True)).exists():
                model_medicamento = Medicamento.objects.get(Q(nombre__icontains=_nombre) & Q(estado=True))
                model_receta = Receta(recomendacion=_recomendacion, fk_medicamento=model_medicamento,
                                      fk_historialclinico=model_historial_clinico)
                model_receta.save()
                model_historial_clinico.estado_receta = existsReceta(model_historial_clinico)
                model_historial_clinico.save()
            else:
                model_medicamento = Medicamento(nombre=_nombre)
                model_medicamento.save()
                model_receta = Receta(recomendacion=_recomendacion, fk_medicamento=model_medicamento,
                                      fk_historialclinico=model_historial_clinico)
                model_receta.save()
                model_historial_clinico.estado_receta = existsReceta(model_historial_clinico)
                model_historial_clinico.save()
            model_receta = Receta.objects.filter(Q(estado=True) & Q(fk_historialclinico=model_historial_clinico))
            datalist_medicamento = Medicamento.objects.filter(estado=True)
            return render(request, 'Clinic/Receta/create_receta.html',
                          {'model_receta': model_receta, 'datalist_medicamento': datalist_medicamento,
                           'model_historial_clinico': model_historial_clinico})
        else:
            model_historial_clinico.estado_receta = existsReceta(model_historial_clinico)
            model_historial_clinico.save()
            model_receta = Receta.objects.filter(Q(estado=True) & Q(fk_historialclinico=model_historial_clinico))
            datalist_medicamento = Medicamento.objects.filter(estado=True)
            return render(request, 'Clinic/Receta/create_receta.html',
                          {'model_receta': model_receta, 'datalist_medicamento': datalist_medicamento,
                           'model_historial_clinico': model_historial_clinico})

def report_receta(request, pk_historial_clinico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_historial_clinico = HistorialClinico.objects.get(pk_historial_clinico=pk_historial_clinico)
        model_historial_clinico.estado_receta = existsReceta(model_historial_clinico)
        model_historial_clinico.save()
        model_receta = Receta.objects.filter(Q(estado=True) & Q(fk_historialclinico=model_historial_clinico))
        datalist_medicamento = Medicamento.objects.filter(estado=True)
        return render(request, 'Clinic/Receta/report_receta.html',
                      {'model_receta': model_receta, 'datalist_medicamento': datalist_medicamento,
                       'model_historial_clinico': model_historial_clinico})

def delete_receta(request, pk_receta, pk_historial_clinico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_receta = Receta.objects.get(pk_receta=pk_receta)
        model_receta.estado = False
        model_receta.delete()
        return redirect('clinic:create_receta', pk_historial_clinico)


def existsReceta(model_historial_clinico):
    if Receta.objects.filter(Q(estado=True) & Q(fk_historialclinico=model_historial_clinico)).exists():
        return True
    else:
        return False


"""
 -- CRUD TO THE MODEL PREGUNTA
"""


def create_pregunta(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == 'GET':
            return render(request, 'Clinic/Pregunta/create_pregunta.html')
        else:
            _descripcion = request.POST.get('descripcion')
            model_pregunta = Pregunta(descripcion=_descripcion)
            model_pregunta.save()
            return redirect('clinic:read_pregunta')


def read_pregunta(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.filter(estado=True)
        _descripcion = request.GET.get('descripcion')
        if _descripcion:
            model_pregunta = Pregunta.objects.filter(Q(estado=True) & Q(descripcion__icontains=_descripcion))

        return render(request, 'Clinic/Pregunta/read_pregunta.html', {'model_pregunta': model_pregunta})


def update_pregunta(request, pk_pregunta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.get(pk_pregunta=pk_pregunta)
        if request.method == 'GET':
            return render(request, 'Clinic/Pregunta/update_pregunta.html', {'model_pregunta': model_pregunta})
        else:
            _descripcion = request.POST.get('descripcion')
            model_pregunta.descripcion = _descripcion
            model_pregunta.save()
            return redirect('clinic:read_pregunta')


def delete_pregunta(request, pk_pregunta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_pregunta = Pregunta.objects.get(pk_pregunta=pk_pregunta)
        model_pregunta.estado = False
        model_pregunta.save()
        return redirect('clinic:read_pregunta')


"""
 -- CRUD TO THE MODEL SERVICIO
"""


def create_servicio(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == 'GET':
            return render(request, 'Clinic/Servicio/create_servicio.html')
        else:
            _nombre = request.POST.get('nombre')
            _brev_descripcion = request.POST.get('brev_descripcion')
            model_servicio = Servicio(nombre=_nombre, brev_descripcion=_brev_descripcion)
            model_servicio.save()
            return redirect('clinic:read_servicio')


def read_servicio(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_servicio = Servicio.objects.filter(estado=True)
        _nombre = isStr(request.GET.get('nombre'))
        if _nombre:
            model_servicio = Servicio.objects.filter(Q(estado=True) & Q(nombre__icontains=_nombre))

        return render(request, 'Clinic/Servicio/read_servicio.html', {'model_servicio': model_servicio})


def update_servicio(request, pk_servicio):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_servicio = Servicio.objects.get(pk_servicio=pk_servicio)
        if request.method == 'GET':
            return render(request, 'Clinic/Servicio/update_servicio.html', {'model_servicio': model_servicio})
        else:
            _nombre = request.POST.get('nombre')
            _brev_descripcion = request.POST.get('brev_descripcion')
            model_servicio.nombre = _nombre
            model_servicio.brev_descripcion = _brev_descripcion
            model_servicio.save()
            return redirect('clinic:read_servicio')


def delete_servicio(request, pk_servicio):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        model_servicio = Servicio.objects.get(pk_servicio=pk_servicio)
        model_servicio.estado = False
        model_servicio.save()
        return redirect('clinic:read_servicio')


"""
 -- CRUD TO THE MODEL CONTROL-CLINIC
"""


def control_clinica(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        try:
            model_control_clinica = ControlClinica.objects.filter(estado=True)[:1].get()
        except ObjectDoesNotExist:
            model_control_clinica = ControlClinica(nombre="ClinicaDrPineda", estado_servicio=True, estado=True)
            model_control_clinica.save()
        return render(request, 'Clinic/ControlClinica/control_clinica.html',
                      {'model_control_clinica': model_control_clinica})


def estado_servicio_control_clinica(request, estado_servicio):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if estado_servicio == 1:
            model_control_clinica = ControlClinica.objects.filter(estado=True)[:1].get()
            model_control_clinica.estado_servicio = True
            model_control_clinica
        else:
            model_control_clinica = ControlClinica.objects.filter(estado=True)[:1].get()
            model_control_clinica.estado_servicio = False
            model_control_clinica
        model_control_clinica.save()
        return redirect('clinic:control_clinica')


"""
 -- SISTEM TUTORIALS
"""


def tutorial_paciente(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_paciente.html')


def tutorial_cita(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_cita.html')


def tutorial_medicamento(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_medicamento.html')


def tutorial_historial_medico(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_historial_medico.html')


def tutorial_pregunta_nps(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_pregunta_nps.html')


def tutorial_servicio(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_servicio.html')


def tutorial_clinica(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        return render(request, 'Clinic/Tutorial/tutorial_clinica.html')
