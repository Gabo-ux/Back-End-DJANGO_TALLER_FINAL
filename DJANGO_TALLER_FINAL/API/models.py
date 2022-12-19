from django.db import models

# Create your models here.

class Inscripciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    fecha = models.DateField()
    institucion =  models.CharField(max_length=50)
    hora = models.TimeField()
    estado = models.CharField(max_length=20)
    observacion = models.TextField(blank=True)
