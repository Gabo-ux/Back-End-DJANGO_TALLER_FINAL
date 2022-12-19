from django import forms
from CRUD.models import Inscripciones

class Forminscripcion(forms.ModelForm):
    class Meta:
        model = Inscripciones
        fields = '__all__'