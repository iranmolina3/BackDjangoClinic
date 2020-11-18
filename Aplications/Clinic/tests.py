from django.test import TestCase, Client
from .models import *
from datetime import datetime


class TestModels(TestCase):

    def setUp(self):
        self.persona = Persona.objects.create(nombre="Iran", apellido="Molina", dpi="_dpi", edad=18,
                                              fecha_nacimiento=datetime.today().strftime("%Y-%m-%d"),
                                              telefono="88885555", genero="Masculino",
                                              direccion="Barrio agua caliente", municipio="Salama",
                                              estado_civil="Soltero(a)",
                                              hora_inicio=datetime.today().strftime("%Y-%m-%dT%H:%M"),
                                              hora_final=datetime.today().strftime("%Y-%m-%dT%H:%M"))

    def test_persona_is_assigned_slug_on_creation(self):
        self.assertEqual(self.persona.nombre, 'Iran')

