from django.db import models
from django.core.validators import EmailValidator
from .validators import validate_anio_mes
from .validators import validate_idioma_permitido

class CurriculumVitae(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)    
    correo = models.EmailField(validators=[EmailValidator('Correo no válido'),])    
    perfil = models.TextField()
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class Formacion(models.Model):
    curriculum_vitae = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    nombre_entidad = models.CharField(max_length=250)    
    grado = models.CharField(max_length=100)    
    desde = models.CharField(max_length=7, validators=[validate_anio_mes,])
    hasta = models.CharField(max_length=7, validators=[validate_anio_mes,])
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.nombre_entidad} ({self.desde} a {self.hasta})"
    
class ExperienciaLaboral(models.Model):
    curriculum_vitae = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=250)
    empresa = models.CharField(max_length=250)
    desde = models.CharField(max_length=7, validators=[validate_anio_mes,])
    hasta = models.CharField(max_length=7, validators=[validate_anio_mes,])
    descripcion = models.TextField()
    
    def __str__(self):
        return f"{self.cargo} - {self.empresa} ({self.desde} a {self.hasta})"
    
class Experiencias(models.TextChoices):
    PRINCIPIANTE = 'principiante', 'Principiante'
    MEDIO = 'medio', 'Medio'
    HABIL = 'habil', 'Hábil'
    AVANZADO = 'avanzado', 'Avanzado'
    EXPERTO = 'experto', 'Experto'
    
class Habilidad(models.Model):
    curriculum_vitae = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=250)
    experiencias = models.CharField(
        max_length=12,
        choices=Experiencias.choices,
        default=Experiencias.PRINCIPIANTE
    )
    
    def __str__(self):
        return self.nombre
    
class Niveles(models.TextChoices):
    BASICO = 'basico', 'Básico'
    MEDIO = 'medio', 'Medio'
    AVANZADO = 'avanzado', 'Avanzado'    

class Idioma(models.Model):
    curriculum_vitae = models.ForeignKey(CurriculumVitae, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, validators=[validate_idioma_permitido,])
    niveles = models.CharField(
        max_length=8,
        choices=Niveles.choices,
        default=Niveles.BASICO
    )
    
    def __str__(self):
        return self.nombre