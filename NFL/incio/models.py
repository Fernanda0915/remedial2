from django.db import models

class Equipos(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
      verbose_name_plural = 'EQUIPOS'
    def __str__(self):
        return self.nombre


class jugadores(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'JUGADORES'


class Estadio(models.Model):
    nombre = models.CharField(max_length=100)
    jugadores = models.ForeignKey(Jugadores, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipos, on_delete=models.CASCADE)
    
    class Meta:
            verbose_name_plural = 'ESTADIO'
    def __str__(self):
        return self.nombre