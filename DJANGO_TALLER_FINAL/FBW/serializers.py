from rest_framework import serializers
from .models import Instituciones

class InstitucionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituciones
        fields = '__all__'