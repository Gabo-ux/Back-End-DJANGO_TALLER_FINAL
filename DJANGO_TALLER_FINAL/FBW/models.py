from django.db import models

# Create your models here.

class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)

