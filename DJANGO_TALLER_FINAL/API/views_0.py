from django.shortcuts import render
from django.http import JsonResponse
from API.models import Inscripciones

# Create your views here.


def verinscritos(request):
    ins = {
            'Id': 1,
            'Nombre': 'Julian',
            'Telefono': '+56923674589',
            'Fecha': '2022-09-09',
            'institucion': 'Banco Estado',
            'Hora': '14:23:42',
            'Estado': 'RESERVADA',
            'Observacion': ''
        }
    return JsonResponse(ins)
