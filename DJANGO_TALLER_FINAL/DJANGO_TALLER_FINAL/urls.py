"""DJANGO_TALLER_FINAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API import views_0
from CBW import views_1
from CRUD import views_2
from FBW import views_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_2.index),
    path('API/inscripciones/', views_0.verinscritos),
    path('CBW/inscripciones/<int:pk>', views_1.DetalleInscripciones.as_view()),
    path('CBW/inscripciones/', views_1.ListarInscripciones.as_view()),
    path('CRUD/inscripciones/', views_2.listar_Inscripciones),
    path('CRUD/agregarinscripcion/', views_2.agregar_inscripcion),
    path('CRUD/eliminar/<int:id>', views_2.eliminar_inscripcion),
    path('CRUD/actualizar/<int:id>', views_2.actualizar_inscripcion),
    path('FBW/instituciones/', views_3.Instituciones_list),
    path('FBW/instituciones/<int:id>', views_3.Instituciones_detalle),
]
