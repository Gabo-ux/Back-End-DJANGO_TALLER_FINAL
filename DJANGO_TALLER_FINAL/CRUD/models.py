from django.db import models

# Create your models here.

ESTADO = (
    ('reservada','RESERVADA'),
    ('completada','COMPLETADA'),
    ('anulada','ANULADA'),
    ('no asiste','NO ASISTE'),
)

class Inscripciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    fecha = models.DateField()
    institucion =  models.CharField(max_length=50)
    hora = models.TimeField(auto_now=False)
    estado = models.CharField(max_length=20, choices=ESTADO, default='no asiste')
    observacion = models.TextField(blank=True)