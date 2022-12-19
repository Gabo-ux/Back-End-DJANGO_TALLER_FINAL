from rest_framework import serializers
from .models import Inscripciones

class InscripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripciones
        fields = '__all__'