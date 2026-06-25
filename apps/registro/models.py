from django.db import models
from apps.categoria.models import Categoria

class Registro(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'ganancia'),
        ('egreso', 'gasto'),
    ]
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    tipo = models.CharField(max_length=7, choices=TIPO_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='registros')

    def __str__(self):
        return f"{self.tipo} - ${self.total} ({self.categoria.nombre})"

