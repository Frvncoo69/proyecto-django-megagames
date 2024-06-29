from django.db import models

class juego(models.Model):
    id=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=6, decimal_places=2)
    imagen=models.ImageField(upload_to='juegos/',null=True, blank=True)
    descripcion=models.TextField()
    stock=models.IntegerField(default=0)

def __str__(self):
    return self.nombre