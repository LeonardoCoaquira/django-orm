from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta_texto = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.pregunta_texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion_texto = models.CharField(max_length=255)
    puntos = models.IntegerField(default=0)
    
    def __str__(self):
        return self.opcion_texto