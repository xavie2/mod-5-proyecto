from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"curriculums", views.CurriculumVitaeViewSet)

urlpatterns = [
    # path("", views.index, name="index")    
    path('curriculum/crear/', views.CurriculumVitaeCreateView.as_view()),
    path("curriculums/cantidad", views.curriculum_count),
    path("curriculums/buscar", views.curriculum_buscar_apellido),
    path('', include(router.urls)),
]
