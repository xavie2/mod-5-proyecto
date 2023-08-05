from django.contrib import admin
from .models import CurriculumVitae
from .models import Formacion
from .models import ExperienciaLaboral
from .models import Habilidad
from .models import Idioma

# Curriculum Vitae
class CurriculumVitaeAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres', 'correo')
    list_filter = ('apellidos', 'nombres', 'correo')
    search_fields = ('apellidos', 'nombres', 'correo')
    ordering = ('apellidos', 'nombres')

admin.site.register(CurriculumVitae, CurriculumVitaeAdmin)

admin.site.register(Formacion)
admin.site.register(ExperienciaLaboral)
admin.site.register(Habilidad)
admin.site.register(Idioma)
