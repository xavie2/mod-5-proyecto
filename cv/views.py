from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import CurriculumVitae
from .models import Formacion
from .models import Idioma

from .serializers import CurriculumVitaeSerializer
from .serializers import FormacionSerializer
from .serializers import IdiomaSerializer

class CurriculumVitaeViewSet(viewsets.ModelViewSet):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer
    
class CurriculumVitaeCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = CurriculumVitae.objects.all()
    serializer_class = CurriculumVitaeSerializer

class FormacionViewSet(viewsets.ModelViewSet):
    queryset = Formacion.objects.all()
    serializer_class = FormacionSerializer
    
class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer
    
def curriculum_count(request):
    try:
        cantidad = CurriculumVitae.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200
        )
    except:
      return JsonResponse({"mensaje": str(e)}, status=400)
  
def curriculum_buscar_apellido(request):
    try:
        q = request.GET.get('q')
        if q:
            curriculums = CurriculumVitae.objects.filter(apellidos__icontains=q)
        else:
            curriculums = CurriculumVitae.objects.all()
        
        return JsonResponse(
            CurriculumVitaeSerializer(curriculums, many=True).data,
            safe=False,
            status=200
        )
    except:
      return JsonResponse({"mensaje": str(e)}, status=400)