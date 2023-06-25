from django.db import models

# Create your models here.
class Parroquia(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, choices=(('urbana', 'Urbana'), ('rural', 'Rural')))

    def __str__(self):
        return "Parroquia: %s - %s" % (self.nombre, self.tipo)
    

class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    nro_viviendas = models.IntegerField()
    nro_parques = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')))
    nro_edificios = models.IntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name="barrios")

    def __str__(self):
        return "Barrio: %s - %d - %d - %d" % (self.nombre, self.nro_viviendas, self.nro_parques, self.nro_edificios)