from cv import validators
from rest_framework import serializers
from .models import CurriculumVitae
from .models import Formacion
from .models import Idioma
from .validators import validate_anio_mes
from .validators import validate_idioma_permitido


class CurriculumVitaeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurriculumVitae
        fields = "__all__"
        
class FormacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formacion
        fields = "__all__"

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = "__all__"