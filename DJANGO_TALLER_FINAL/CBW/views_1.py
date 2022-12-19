from django.shortcuts import render
from .serializers import InscripcionesSerializer
from .models import Inscripciones
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class ListarInscripciones(APIView):
    def get(self, request):
        ins = Inscripciones.objects.all()
        serial = InscripcionesSerializer(ins, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = InscripcionesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleInscripciones(APIView):

    def get_object(self, pk):
        try:
            return Inscripciones.objects.get(pk=pk)
        except Inscripciones.DoesNotExist:
            return Http404

    def get(self, request, pk):
        ins = self.get_object(pk)
        serial = InscripcionesSerializer(ins)
        return Response(serial.data)
    
    def put(self, request, pk):
        ins = self.get_object(pk)
        serial = InscripcionesSerializer(ins, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ins = self.get_object(pk)
        ins.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)