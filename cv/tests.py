from django.test import TestCase
from .models import CurriculumVitae
from .models import Formacion
from .models import Idioma
from django.core.exceptions import ValidationError

class TestCurriculumVitaes(TestCase):
    def test_campos_obligatorios(self):
        with self.assertRaises(ValidationError):
            cv = CurriculumVitae()
            cv.full_clean()
            
    def test_grabacion(self):
        cv = CurriculumVitae(nombres="Franz Javier", apellidos="Muraña Cruz", correo="xavie2@gmail.com", perfil="Mi perfil")
        cv.save()
        self.assertEqual(cv.nombres, "Franz Javier")
        
    def test_correo_valido(self):
        cv = CurriculumVitae(nombres="Alex Santos", apellidos="Chavez Estrada", correo="alexgmail.com", perfil="Mi perfil")
        cv.full_clean()
        
