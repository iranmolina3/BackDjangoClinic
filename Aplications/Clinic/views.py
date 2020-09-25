from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import date
from random import choice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# -- METHOD -- > THIS IS OTHER FUNCTIONS (NOT VIEWS ONLY LOAD DATA)


# -- METHOD -- > This is a functions to logout the system

def logout_view(request):
    logout(request)
    return redirect('index')

# -- METHOD -- > this is a funtions for load the number citas

def span_numero_citas():
    fecha_ingreso = date.today()
    cita = Cita.objects.filter(ESTADO=True, FECHA_INGRESO=fecha_ingreso)
    contador = 0
    for lista_cita in cita:
        contador = contador + 1
    return contador

# -- METHOD -- > this is a functions for generate the password

def generator_password():
    #   generador de contrasenia
    longitud = 8
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    _password = ""
    _password = _password.join([choice(valores) for i in range(longitud)])
    print("CONTRASENIA DE USUARIO ", _password)
    return _password

# -- METHOD -- > this is functions for init the options users

def generator_carnet(_nombre, contador):
    #   generador de usuario con contador if a same user
    year = date.today().strftime("%Y")
    usuario = Usuario.objects.filter(ESTADO=True, CARNET__regex=str(_nombre) + str(year))
    print()
    for lista_usuario in usuario:
        print(lista_usuario)
        contador = contador + 1
    _carnet = str(_nombre) + str(year) + str(contador)
    return _carnet

# -- METHOD CREATE PERSONA -- this is a functions to create a HISTORIAL PACIENTE pass this to (TRUE)

def create_persona_hitorial(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
            print(request.POST)
            _nombre1 = request.POST.get('NOMBRE1')
            _nombre2 = request.POST.get('NOMBRE2')
            _nombre = _nombre1 + ' ' + _nombre2
            _apellido1 = request.POST.get('APELLIDO1')
            _apellido2 = request.POST.get('APELLIDO2')
            _apellido = _apellido1 + ' ' + _apellido2
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
            print(_dpi, _edad, _genero, _nombre, _apellido, _direccion, _fecha_nac, _fk_estado_civil, estado_civil,
                  municipio, _telefono)
            _model_persona = Persona(NOMBRE=_nombre,
                                     APELLIDO=_apellido,
                                     DPI=_dpi,
                                     EDAD=_edad,
                                     FECHA_NACIMIENTO=_fecha_nac,
                                     TELEFONO=_telefono,
                                     GENERO=_genero,
                                     DIRECCION=_direccion,
                                     FK_MUNICIPIO=municipio,
                                     FK_ESTADO_CIVIL=estado_civil)
            _model_persona.save()
            return _model_persona



# -- INDEX -- VIEW -- > this is the VIEW for the index

def home(request):
    numero = span_numero_citas()
    modelcontrolclinica = ControlClinica.objects.get(estado=True)
    return render(request, 'index.html', {'numero': numero, 'modelcontrolclinica':modelcontrolclinica})

# -- LOGIN -- VIEW -- > this is a functions to begin the system

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
    return render(request, 'login.html')

# -- VIEW -- this is functions for init the options users

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        cita1 = Cita.objects.filter(ESTADO=True, FECHA_INGRESO=date.today()).order_by('FECHA_INGRESO')
        cita2 = Cita.objects.filter(ESTADO=True).order_by('FECHA_INGRESO').exclude(FECHA_INGRESO=date.today())
        paginator = Paginator(cita1, 10)
        page = request.GET.get('page')
        cita1 = paginator.get_page(page)
        return render(request, 'dashboard.html', {'cita1': cita1, 'cita2': cita2})

# -- PERSONA -- VIEW CREATE -- > this is a functions for create a paciente

def create_persona(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
            print(request.POST)
            _nombre1 = request.POST.get('NOMBRE1')
            _nombre2 = request.POST.get('NOMBRE2')
            _nombre = _nombre1 + ' ' + _nombre2
            _apellido1 = request.POST.get('APELLIDO1')
            _apellido2 = request.POST.get('APELLIDO2')
            _apellido = _apellido1 + ' ' + _apellido2
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
            print(_dpi, _edad, _genero, _nombre, _apellido, _direccion, _fecha_nac, _fk_estado_civil, estado_civil,
                  municipio, _telefono)
            _model_persona = Persona(NOMBRE=_nombre,
                                     APELLIDO=_apellido,
                                     DPI=_dpi,
                                     EDAD=_edad,
                                     FECHA_NACIMIENTO=_fecha_nac,
                                     TELEFONO=_telefono,
                                     GENERO=_genero,
                                     DIRECCION=_direccion,
                                     FK_MUNICIPIO=municipio,
                                     FK_ESTADO_CIVIL=estado_civil)
            _model_persona.save()
    #        _carnet = generator_carnet(_nombre1, 1)
    #        _password = generator_password()
    #  ---   select rol Pk 1 becouse been paciente
    #        rol = Rol.objects.get(PK_ROL=1)
    #        user = User.objects.create_user(_carnet, 'ejemplo@gmail.com', _password)
    #        user.first_name = _nombre
    #        user.last_name = _apellido
    #        user.save()
    #        usuario = Usuario(CARNET=_carnet, CONTRASENIA=_password, FK_PERSONA=_model_persona, FK_ROL=rol)
    #        usuario.save()
            return redirect('dashboard')
        municipio = Municipio.objects.filter(ESTADO=True)
        estado_civil = EstadoCivil.objects.filter(ESTADO=True)
        return render(request, 'Clinic/Persona/create_persona.html', {'municipio': municipio, 'estado_civil': estado_civil})

# -- PERSONA -- VIEW LIST -- > this is a functions to list Pacientes

def read_persona(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        persona = Persona.objects.filter(ESTADO=True)
        paginator = Paginator(persona, 6)
        page = request.GET.get('page')
        persona = paginator.get_page(page)
        return render(request, 'Clinic/Persona/read_persona.html', {'persona': persona})

# -- PERSONA -- VIEW UPDATE -- > this is a functions to update data all paciente

def update_persona(request, pk_persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        persona = Persona.objects.get(PK_PERSONA=pk_persona)
        if (request.method == "GET"):
            municipio = Municipio.objects.filter(ESTADO=True)
            estado_civil = EstadoCivil.objects.filter(ESTADO=True)
            fecha_nacimiento = persona.FECHA_NACIMIENTO.strftime("%Y-%m-%d")
            print(fecha_nacimiento)
            return render(request, 'Clinic/Persona/update_persona.html',
                          {'persona': persona, 'estado_civil': estado_civil, 'municipio': municipio,
                           'fecha_nacimiento': fecha_nacimiento})
        else:
            _nombre1 = request.POST.get('NOMBRE1')
            _nombre2 = request.POST.get('NOMBRE2')
            _nombre = _nombre1 + ' ' + _nombre2
            _apellido1 = request.POST.get('APELLIDO1')
            _apellido2 = request.POST.get('APELLIDO2')
            _apellido = _apellido1 + ' ' + _apellido2
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
            return persona

# -- PERSONA -- DELETE VIEW -- > this is a functions to delete (deactivate FALSE)

def delete_persona(request, pk_persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        persona = Persona.objects.get(PK_PERSONA=pk_persona)
        if (request.method == "GET"):
            return render(request, 'Clinic/Persona/delete_persona.html', {'persona': persona})
        else:
            persona.ESTADO = False
            persona.save()
            return redirect('dashboard')

# -- CONSULTA -- VIEW CREATE -- > this is a functions to create a consulta

def create_consulta(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
            #        print(request.POST)
            _motivo_consulta = request.POST.get('MOTIVO_CONSULTA')
            _historia = request.POST.get('HISTORIA')
            print(_motivo_consulta, _historia)
            _model_consulta = Consulta(MOTIVO_CONSULTA=_motivo_consulta,
                                       HISTORIA=_historia)
            _model_consulta.save()
            return _model_consulta

# -- CONSULTA -- VIEW LIST -- > this is a functions to show the data CONSULTAS HISTORIAL

def read_consulta(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        consulta = Consulta.objects.filter(ESTADO=True)
        print(consulta)
        paginator = Paginator(consulta, 6)
        page = request.GET.get('page')
        consulta = paginator.get_page(page)
        return render(request, 'Clinic/Consulta/read_consulta.html', {'consulta': consulta})

# -- CONSULTA -- VIEW UPDATE -- > this is a functions to update the data CONSULTA

def update_consulta(request, pk_consulta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        consulta = Consulta.objects.get(PK_CONSULTA=pk_consulta)
        if (request.method == "GET"):
            return render(request, 'Clinic/Consulta/update_consulta.html', {'consulta': consulta})
        else:
            _motivo_consulta = request.POST.get('MOTIVO_CONSULTA')
            _historia = request.POST.get('HISTORIA')
            consulta.MOTIVO_CONSULTA = _motivo_consulta
            consulta.HISTORIA = _historia
            consulta.save()
            return redirect('dashboard')

# -- CONSULTA -- VIEW DELETE -- > this is a functions to deactivate (pass FALSE)

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

# -- EXAMEN_FISICO -- VIEW CREATE -- > this is a functions to EXAMEN FISICO

def create_examen_fisico(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
            #        print(request.POST)
            _presion_arterial = request.POST.get('PRESION_ARTERIAL')
            _frecuencia_cardiaca = request.POST.get('FRECUENCIA_CARDIACA')
            _frecuencia_respiratoria = request.POST.get('FRECUENCIA_RESPIRATORIA')
            _temperatura = request.POST.get('TEMPERATURA')
            _frecuencia_cardiaca_fetal = request.POST.get('FRECUENCIA_CARDIACA_FETAL')
            _impresion_clinica = request.POST.get('IMPRESION_CLINCIA')
            print(_presion_arterial, _frecuencia_cardiaca, _frecuencia_respiratoria, _temperatura,
                  _frecuencia_cardiaca_fetal, _impresion_clinica)
            _model_examen_fisico = ExamenFisico(PRESION_ARTERIAL=_presion_arterial,
                                                FRECUENCIA_CARDIACA=_frecuencia_cardiaca,
                                                FRECUENCIA_RESPIRATORIA=_frecuencia_respiratoria, TEMPERATURA=_temperatura,
                                                FRECUENCIA_CARDIACA_FETAL=_frecuencia_cardiaca_fetal,
                                                IMPRESION_CLINCIA=_impresion_clinica)
            _model_examen_fisico.save()
            return _model_examen_fisico

# -- EXAMEN_FISICO -- VIEW READ -- >  this is a functions to show data EXAMEN FISICO

def read_examen_fisico(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        examen_fisico = ExamenFisico.objects.filter(ESTADO=True)
        print(examen_fisico)
        paginator = Paginator(examen_fisico, 6)
        page = request.GET.get('page')
        examen_fisico = paginator.get_page(page)
        return render(request, 'Clinic/ExamenFisico/read_examen_fisico.html', {'examen_fisico': examen_fisico})

# -- EXAMEN_FISICO -- VIEW UPDATE -- > this is a funtcions updata data

def update_examen_fisico(request, pk_examen_fisico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        examen_fisico = ExamenFisico.objects.get(PK_EXAMEN_FISICO=pk_examen_fisico)
        if (request.method == "GET"):
            return render(request, 'Clinic/ExamenFisico/update_examen_fisico.html', {'examen_fisico': examen_fisico})
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

# -- EXAMEN_FISICO -- VIEW DELETE -- > this is a functions to deactivate ExamenFisico

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

# -- ANTECEDENTE -- VIEW CREATE -- > this is a functions to create ANTECEDENTE

def create_antecedente(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
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
            _model_antecedente = Antecedente(ULTIMA_REGLA=_ultima_regla, FECHA_PROBABLE_PARTO=_fecha_probable_parto,
                                             GESTA=_gesta, ABORTO=_aborto, HIJOS_VIVOS=_hijos_vivos,
                                             PESO=_peso, QUIRURGICO=_quirurgico, MEDICO=_medico, ALERGIA=_alergia,
                                             FAMILIAR=_familiar, HABITO=_habito, CIGARRO=_cigarro,
                                             LICOR=_licor)
            _model_antecedente.save()
            return _model_antecedente

# -- ANTECEDENTE -- VIEW LIST -- > this is a functions to show data list Antecedente

def read_antecedente(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        antecedente = Antecedente.objects.filter(ESTADO=True)
        paginator = Paginator(antecedente, 6)
        page = request.GET.get('page')
        antecedente = paginator.get_page(page)
        return render(request, 'Clinic/Antecedente/read_antecedente.html', {'antecedente': antecedente})

# -- ANTECEDENTE -- VIEW UPDATE -- > this is a functions to update data Antecedente

def update_antecedente(request, pk_antecedente):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        antecedente = Antecedente.objects.get(PK_ANTECEDENTE=pk_antecedente)
        if (request.method == "GET"):
            fecha_ultima_regla = antecedente.ULTIMA_REGLA.strftime("%Y-%m-%dT%H:%M")
            fecha_probable_parto = antecedente.FECHA_PROBABLE_PARTO.strftime("%Y-%m-%dT%H:%M")
            gesta = antecedente.GESTA.strftime("%Y-%m-%dT%H:%M")
            aborto = antecedente.ABORTO.strftime("%Y-%m-%dT%H:%M")
            print("CONVERSION FECHA Y HORA =", fecha_ultima_regla)
            return render(request, 'Clinic/Antecedente/update_antecedente.html',
                          {'antecedente': antecedente,
                           'fecha_ultima_regla': fecha_ultima_regla,
                           'fecha_probable_parto': fecha_probable_parto,
                           'gesta': gesta,
                           'aborto': aborto})
        else:
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
            antecedente.ULTIMA_REGLA = _ultima_regla
            antecedente.FECHA_PROBABLE_PARTO = _fecha_probable_parto
            antecedente.GESTA = _gesta
            antecedente.ABORTO = _aborto
            antecedente.HIJOS_VIVOS = _hijos_vivos
            antecedente.PESO = _peso
            antecedente.QUIRURGICO = _quirurgico
            antecedente.MEDICO = _medico
            antecedente.ALERGIA = _alergia
            antecedente.FAMILIAR = _familiar
            antecedente.HABITO = _habito
            antecedente.CIGARRO = _cigarro
            antecedente.LICOR = _licor
            antecedente.save()
            return redirect('dashboard')

# -- ANTECEDENTE -- VIEW DELETE -- > this is a functions to deactivate (FALSE)

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

# -- CITA -- VIEW CREATE -- > this is a functions to create CITA

def create_cita(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == 'GET':
            persona = Persona.objects.filter(ESTADO=True)
            paginator = Paginator(persona, 6)
            page = request.GET.get('page')
            persona = paginator.get_page(page)
            return render(request, 'Clinic/Cita/read_cita.html', {'persona': persona})
        else:
            nombre = request.POST.get("NOMBRE")
            apellido = request.POST.get("APELLIDO")
            persona = Persona.objects.filter(Q(ESTADO=True), Q(NOMBRE__icontains=nombre), Q(APELLIDO__icontains=apellido))
            paginator = Paginator(persona, 6)
            page = request.GET.get('page')
            persona = paginator.get_page(page)
            return render(request, 'Clinic/Cita/read_cita.html', {'persona': persona})

# -- CITA -- VIEW LIST -- > this is a functions to show data CITA

def create_buscar(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == 'GET':
            persona = Persona.objects.filter(ESTADO=True)
            paginator = Paginator(persona, 6)
            page = request.GET.get('page')
            persona = paginator.get_page(page)
            return render(request, 'Clinic/Cita/read_cita.html', {'persona': persona})
        else:
            nombre = request.POST.get("NOMBRE")
            apellido = request.POST.get("APELLIDO")
            persona = Persona.objects.filter(Q(ESTADO=True), Q(NOMBRE__icontains=nombre), Q(APELLIDO__icontains=apellido))
            paginator = Paginator(persona, 6)
            page = request.GET.get('page')
            persona = paginator.get_page(page)
            return render(request, 'Clinic/Cita/read_cita.html', {'persona': persona})


# -- METHOD -- > this is a method to generate a number CITA

def numero_cita(fecha_ingreso):
    print(fecha_ingreso)
    cita = Cita.objects.filter(FECHA_INGRESO=fecha_ingreso)
    contador = 0
    for lista_cita in cita:
        contador = contador + 1
    return contador

# -- CITA -- VIEW CREATE -- > this is a functions to create a CITA

def create_cita(request, pk_persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        persona = Persona.objects.get(PK_PERSONA=pk_persona)
        if request.method == 'GET':
            return render(request, 'Clinic/Cita/create_cita.html', {'persona': persona})
        else:
            fecha_ingreso = request.POST.get('FECHA_INGRESO')
            numero = numero_cita(fecha_ingreso)
            cita = Cita(NUMERO=numero, FECHA_INGRESO=fecha_ingreso, FK_PERSONA=persona)
            cita.save()
            return redirect('dashboard')

# -- CITA -- VIEW DELETE -- > this is a functions to deactivate (FALSE CITA)

def delete_cita(request, pk_cita):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        cita = Cita.objects.get(PK_CITA=pk_cita)
        print(cita)
        if request.method == "GET":
            return render(request, 'Clinic/Cita/delete_cita.html')
        else:
            tipo_estado = TipoEstado.objects.get(NOMBRE='Cancelado')
            cita.ESTADO = False
            cita.FK_TIPO_ESTADO = tipo_estado
            cita.save()
            return redirect('dashboard')

# -- CITA -- VIEW UPDATE -- > this is a functions to update data to Cita

def update_cita(request, pk_cita):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        cita = Cita.objects.get(PK_CITA=pk_cita)
        fecha_ingreso = cita.FECHA_INGRESO.strftime("%Y-%m-%d")
        if (request.method == "GET"):
            return render(request, 'Clinic/Cita/update_cita.html',
                          {'cita': cita, 'fecha_ingreso': fecha_ingreso})
        else:
            _fecha_ingreso = request.POST.get('FECHA_INGRESO')
            numero = numero_cita(_fecha_ingreso)
            cita.NUMERO = numero
            cita.FECHA_INGRESO = _fecha_ingreso
            cita.save()
            return redirect('dashboard')


# -- > SHOW CITAS FROM

# --  -- > query create cita in for list in dashboard

def create_buscar(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        nombre = request.GET.get("NOMBRE")
        persona = Persona.objects.filter(ESTADO=True)
        if nombre:
            persona = Persona.objects.filter(Q(ESTADO=True),
                                             Q(NOMBRE__icontains=nombre) | Q(APELLIDO__icontains=nombre)).distinct()
        paginator = Paginator(persona, 5)
        page = request.GET.get('page')
        persona = paginator.get_page(page)
        return render(request, 'Clinic/Cita/read_cita.html', {'persona': persona})


# < --

# -- > CREATE HISTORIAL - DASHBOARD COMPLETE INFO

# -- > query to menu (completar) in dashboard

def create_historial_clinico(request, pk_cita):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        cita = Cita.objects.get(PK_CITA=pk_cita)
        persona = Persona.objects.get(PK_PERSONA=cita.FK_PERSONA.PK_PERSONA, ESTADO=True)
        if request.method == 'GET':
            if HistorialClinico.objects.filter(ESTADO=True, FK_PERSONA=persona).exists():
                print("HISTORIAL CLINICO - NO VACIO - METHOD GET")
                historial_clinico = HistorialClinico.objects.get(ESTADO=True, FK_PERSONA=persona)
                fecha_nacimiento = persona.FECHA_NACIMIENTO.strftime("%Y-%m-%d")
                nombres = persona.NOMBRE.split(" ")
                apellidos = persona.APELLIDO.split(" ")
                primer_nombre = nombres[0]
                segundo_nombre = nombres[1]
                primer_apellido = apellidos[0]
                segundo_apellido = apellidos[1]

                municipio = Municipio.objects.filter(ESTADO=True)

                estado_civil = EstadoCivil.objects.filter(ESTADO=True)

                consulta = Consulta.objects.get(PK_CONSULTA=historial_clinico.FK_CONSULTA.PK_CONSULTA)

                antecedente = Antecedente.objects.get(PK_ANTECEDENTE=historial_clinico.FK_ANTECEDENTE.PK_ANTECEDENTE)
                fecha_ultima_regla = antecedente.ULTIMA_REGLA.strftime("%Y-%m-%dT%H:%M")
                fecha_probable_parto = antecedente.FECHA_PROBABLE_PARTO.strftime("%Y-%m-%dT%H:%M")
                gesta = antecedente.GESTA.strftime("%Y-%m-%dT%H:%M")
                aborto = antecedente.ABORTO.strftime("%Y-%m-%dT%H:%M")
                print("CONVERSION FECHA Y HORA =", fecha_ultima_regla)

                examen_fisico = ExamenFisico.objects.get(
                    PK_EXAMEN_FISICO=historial_clinico.FK_EXAMEN_FISICO.PK_EXAMEN_FISICO)

                return render(request, 'Clinic/HistorialClinico/create_historial_clinico.html',
                              {'cita': cita, 'persona': persona, 'primer_nombre': primer_nombre,
                               'segundo_nombre': segundo_nombre, 'primer_apellido': primer_apellido,
                               'segundo_apellido': segundo_apellido, 'fecha_nacimiento': fecha_nacimiento,
                               'municipio': municipio, 'estado_civil': estado_civil, 'consulta': consulta,
                               'antecedente': antecedente, 'fecha_ultima_regla': fecha_ultima_regla,
                               'fecha_probable_parto': fecha_probable_parto, 'gesta': gesta, 'aborto': aborto,
                               'examen_fisico': examen_fisico})
            else:
                print("HISTORIAL CLINICO - VACIO - METHOD GET")
                municipio = Municipio.objects.filter(ESTADO=True)
                estado_civil = EstadoCivil.objects.filter(ESTADO=True)
                fecha_nacimiento = persona.FECHA_NACIMIENTO.strftime("%Y-%m-%d")
                nombres = persona.NOMBRE.split(" ")
                apellidos = persona.APELLIDO.split(" ")
                primer_nombre = nombres[0]
                segundo_nombre = nombres[1]
                primer_apellido = apellidos[0]
                segundo_apellido = apellidos[1]
                fecha_ultima_regla = "0001-01-01T00:00"
                fecha_probable_parto = "0001-01-01T00:00"
                gesta = "0001-01-01T00:00"
                aborto = "0001-01-01T00:00"
                return render(request, 'Clinic/HistorialClinico/create_historial_clinico.html',
                              {'cita': cita, 'persona': persona, 'primer_nombre': primer_nombre,
                               'segundo_nombre': segundo_nombre, 'primer_apellido': primer_apellido,
                               'segundo_apellido': segundo_apellido, 'fecha_nacimiento': fecha_nacimiento,
                               'municipio': municipio, 'estado_civil': estado_civil,
                               'fecha_ultima_regla': fecha_ultima_regla,
                               'fecha_probable_parto': fecha_probable_parto, 'gesta': gesta, 'aborto': aborto,
                               })
        else:
            if HistorialClinico.objects.filter(ESTADO=True, FK_PERSONA=persona).exists():
                print('HISTORIAL CLINICO - NO VACIO - METHOD POST')
                _update_historial_clinico = HistorialClinico.objects.get(ESTADO=True, FK_PERSONA=persona)
                _update_historial_clinico.ESTADO = False
                _update_historial_clinico.save()
                persona = Persona.objects.get(PK_PERSONA=cita.FK_PERSONA.PK_PERSONA)
                filtro_nombre_completo = persona.NOMBRE + ' ' + persona.APELLIDO
                persona.ESTADO = False
                persona.save()
                _persona = create_persona_hitorial(request)
                _consulta = create_consulta(request)
                _antecedente = create_antecedente(request)
                _examen_fisico = create_examen_fisico(request)
                _create_historial_clinico = HistorialClinico(FK_CONSULTA=_consulta, FK_EXAMEN_FISICO=_examen_fisico,
                                                             FK_ANTECEDENTE=_antecedente, FK_PERSONA=_persona,
                                                             FILTRO_NOMBRE_COMPLETO=filtro_nombre_completo)
                _create_historial_clinico.save()
                cita.ESTADO = False
                cita.save()
            else:
                print('HISTORIAL CLINICO - VACIO - METHOD POST')
                filtro_nombre_completo = persona.NOMBRE + ' ' + persona.APELLIDO
                _persona = update_persona(request, persona.PK_PERSONA)
                _consulta = create_consulta(request)
                _antecedente = create_antecedente(request)
                _examen_fisico = create_examen_fisico(request)
                _create_historial_clinico = HistorialClinico(FK_CONSULTA=_consulta, FK_EXAMEN_FISICO=_examen_fisico,
                                                             FK_ANTECEDENTE=_antecedente, FK_PERSONA=_persona,
                                                             FILTRO_NOMBRE_COMPLETO=filtro_nombre_completo)
                _create_historial_clinico.save()
                cita.ESTADO = False
                cita.save()
            return redirect('dashboard')


# -- > HISTORIAL CLINIC - LISTAR PEOPLE - HISTORIAL

#  -- > create this function for view person for the histori clinic

def read_historial_clinico(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        nombre = request.GET.get("NOMBRE")
        historial_clinico = HistorialClinico.objects.all().order_by('-ESTADO')
        if nombre:
            historial_clinico = HistorialClinico.objects.filter(Q(FILTRO_NOMBRE_COMPLETO__icontains=nombre)).order_by(
                '-ESTADO')
        paginator = Paginator(historial_clinico, 3)
        page = request.GET.get('page')
        historial_clinico = paginator.get_page(page)
        return render(request, 'Clinic/HistorialClinico/read_historial_clinico.html',
                      {'historial_clinico': historial_clinico})


# --> HISTORIAL CLINIC - UPDATE

# -- > edith is a functions for to update persona

# -- > this funtion is to update only dont create object person

def edit_persona(request, persona):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == "POST":
            _nombre1 = request.POST.get('NOMBRE1')
            _nombre2 = request.POST.get('NOMBRE2')
            _nombre = _nombre1 + ' ' + _nombre2
            _apellido1 = request.POST.get('APELLIDO1')
            _apellido2 = request.POST.get('APELLIDO2')
            _apellido = _apellido1 + ' ' + _apellido2
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
            return persona


# -- > edit this functions is from consulta

def edit_consulta(request, consulta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == "POST":
            _motivo_consulta = request.POST.get('MOTIVO_CONSULTA')
            _historia = request.POST.get('HISTORIA')
            consulta.MOTIVO_CONSULTA = _motivo_consulta
            consulta.HISTORIA = _historia
            consulta.save()

# -- > edit this funtions is from antecedente

def edit_antecedente(request, antecedente):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == "POST":
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
            antecedente.ULTIMA_REGLA = _ultima_regla
            antecedente.FECHA_PROBABLE_PARTO = _fecha_probable_parto
            antecedente.GESTA = _gesta
            antecedente.ABORTO = _aborto
            antecedente.HIJOS_VIVOS = _hijos_vivos
            antecedente.PESO = _peso
            antecedente.QUIRURGICO = _quirurgico
            antecedente.MEDICO = _medico
            antecedente.ALERGIA = _alergia
            antecedente.FAMILIAR = _familiar
            antecedente.HABITO = _habito
            antecedente.CIGARRO = _cigarro
            antecedente.LICOR = _licor
            antecedente.save()

# -- > this funtion is from edit Examen Fisico

def edit_examen_fisico(request, examen_fisico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if (request.method == "POST"):
            _presion_arterial = request.POST.get('PRESION_ARTERIAL')
            _frecuencia_cardiaca = request.POST.get('FRECUENCIA_CARDIACA')
            _frecuencia_respiratoria = request.POST.get('FRECUENCIA_RESPIRATORIA')
            _temperatura = request.POST.get('TEMPERATURA')
            _frecuencia_cardiaca_fetal = request.POST.get('FRECUENCIA_CARDIACA_FETAL')
            _impresion_clinica = request.POST.get('IMPRESION_CLINCIA')
            examen_fisico.PRESION_ARTERIAL = _presion_arterial
            examen_fisico.FRECUENCIA_CARDIACA = _frecuencia_cardiaca
            examen_fisico.FRECUENCIA_RESPIRATORIA = _frecuencia_respiratoria
            examen_fisico.TEMPERATURA = _temperatura
            examen_fisico.FRECUENCIA_CARDIACA_FETAL = _frecuencia_cardiaca_fetal
            examen_fisico.IMPRESION_CLINCIA = _impresion_clinica
            examen_fisico.save()


# -- HISTORIAL_CLINICO -- VIEW UPDATE-- > this methods is to update the 4 tables in the BD

def update_historial_clinico(request, pk_historial_clinico):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        print(pk_historial_clinico)
        historial_clinico = HistorialClinico.objects.get(PK_HISTORIAL_CLINICO=pk_historial_clinico)
        persona = Persona.objects.get(PK_PERSONA=historial_clinico.FK_PERSONA.PK_PERSONA)
        consulta = Consulta.objects.get(PK_CONSULTA=historial_clinico.FK_CONSULTA.PK_CONSULTA)
        antecedente = Antecedente.objects.get(PK_ANTECEDENTE=historial_clinico.FK_ANTECEDENTE.PK_ANTECEDENTE)
        examen_fisico = ExamenFisico.objects.get(PK_EXAMEN_FISICO=historial_clinico.FK_EXAMEN_FISICO.PK_EXAMEN_FISICO)
        if request.method == "GET":
            fecha_nacimiento = persona.FECHA_NACIMIENTO.strftime("%Y-%m-%d")
            nombres = persona.NOMBRE.split(" ")
            apellidos = persona.APELLIDO.split(" ")
            primer_nombre = nombres[0]
            segundo_nombre = nombres[1]
            primer_apellido = apellidos[0]
            segundo_apellido = apellidos[1]

            municipio = Municipio.objects.filter(ESTADO=True)
            estado_civil = EstadoCivil.objects.filter(ESTADO=True)

            fecha_ultima_regla = antecedente.ULTIMA_REGLA.strftime("%Y-%m-%dT%H:%M")
            fecha_probable_parto = antecedente.FECHA_PROBABLE_PARTO.strftime("%Y-%m-%dT%H:%M")
            gesta = antecedente.GESTA.strftime("%Y-%m-%dT%H:%M")
            aborto = antecedente.ABORTO.strftime("%Y-%m-%dT%H:%M")
            print("CONVERSION FECHA Y HORA =", fecha_ultima_regla)

            return render(request, 'Clinic/HistorialClinico/update_historial_clinico.html',
                          {'persona': persona, 'primer_nombre': primer_nombre,
                           'segundo_nombre': segundo_nombre, 'primer_apellido': primer_apellido,
                           'segundo_apellido': segundo_apellido, 'fecha_nacimiento': fecha_nacimiento,
                           'municipio': municipio, 'estado_civil': estado_civil, 'consulta': consulta,
                           'antecedente': antecedente, 'fecha_ultima_regla': fecha_ultima_regla,
                           'fecha_probable_parto': fecha_probable_parto, 'gesta': gesta, 'aborto': aborto,
                           'examen_fisico': examen_fisico})
        else:
            edit_persona(request, persona)
            edit_consulta(request, consulta)
            edit_antecedente(request, antecedente)
            edit_examen_fisico(request, examen_fisico)
            historial_clinico.save()
            return redirect('dashboard')

# -- > CRUD pregunta models

# -- > CREATE for the models Pregunta

def create_pregunta(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        if request.method == 'GET':
            return render(request, 'Clinic/Pregunta/create_pregunta.html')
        else:
            descripcion = request.POST.get('DESCRIPCION')
            pregunta = Pregunta(DESCRIPCION=descripcion)
            pregunta.save()
            return redirect('dashboard')


# -- > READ or select for the models Pregunta

def read_buscar(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        pregunta = Pregunta.objects.filter(ESTADO=True)
        descripcion = request.GET.get('DESCRIPCION')
        if descripcion:
            pregunta = Pregunta.objects.filter(Q(ESTADO=True), Q(DESCRIPCION__icontains=descripcion))
        paginator = Paginator(pregunta, 10)
        page = request.GET.get('page')
        pregunta = paginator.get_page(page)
        return render(request, 'Clinic/Pregunta/read_pregunta.html', {'pregunta': pregunta})


# -- > UPDATE for the update models Pregunta

def update_pregunta(request, pk_pregunta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        pregunta = Pregunta.objects.get(PK_PREGUNTA=pk_pregunta)
        if request.method == 'GET':
            return render(request, 'Clinic/Pregunta/update_pregunta.html', {'pregunta': pregunta})
        else:
            descripcion = request.POST.get('DESCRIPCION')
            pregunta.DESCRIPCION = descripcion
            pregunta.save()
            return redirect('dashboard')

# -- > DELETE for the models Pregunta deactivate

def delete_pregunta(request, pk_pregunta):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        pregunta = Pregunta.objects.get(PK_PREGUNTA=pk_pregunta)
        if request.method == 'GET':
            return render(request, 'Clinic/Pregunta/delete_pregunta.html', {'pregunta': pregunta})
        else:
            pregunta.ESTADO = False
            pregunta.save()
            return redirect('dashboard')

# -- > CRUD for the models Usuario only Read and Update

# -- > READ for the models Usuario dont delete only update

def read_usuario(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        usuario = Usuario.objects.filter(ESTADO=True)
        carnet = request.GET.get("CARNET")
        if carnet:
            usuario = Usuario.objects.filter(Q(ESTADO=True), Q(CARNET__icontains=carnet))
        paginator = Paginator(usuario, 10)
        page = request.GET.get('page')
        usuario = paginator.get_page(page)
        return render(request, 'Clinic/Usuario/read_usuario.html', {'usuario': usuario})

# -- USUARIO -- VIEW UPDATE -- > this is a functions to update data Usuario

def update_usuario(request, pk_usuario):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        usuario = Usuario.objects.get(PK_USUARIO=pk_usuario)
        if request.method == "GET":
            return render(request, 'Clinic/Usuario/update_usuario.html', {'usuario': usuario})
        else:
            usuario.CONTRASENIA = request.POST.get('CONTRASENIA')
            usuario.CORREO = request.POST.get('CORREO')
            usuario.save()
            return redirect('clinic:read_usuario')

# -- control clinic - view select -- > this functions show data clinics

def close_clinica(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        modelcontrolclinica = ControlClinica.objects.get(estado=True)
        if request.method == 'GET':
            return render(request, 'Clinic/ControlClinica/close_clinica.html', {'modelcontrolclinica': modelcontrolclinica})
        else:
            modelcontrolclinica.servicio = False
            modelcontrolclinica.save()
            return redirect('dashboard')

def open_clinica(request):
    if not request.user.is_authenticated:
        return redirect('sing')
    else:
        modelcontrolclinica = ControlClinica.objects.get(estado=True)
        if request.method == 'GET':
            return render(request, 'Clinic/ControlClinica/open_clinica.html', {'modelcontrolclinica': modelcontrolclinica})
        else:
            modelcontrolclinica.servicio = True
            modelcontrolclinica.save()
            return redirect('dashboard')