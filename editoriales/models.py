from django.db import models

# Create your models here.
from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

