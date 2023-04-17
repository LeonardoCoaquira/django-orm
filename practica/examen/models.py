from django.db import models

# Create your models here.
class Examen(models.Model):
    titulo = models.CharField(max_length=255)
    # Otros campos necesarios para el examen, como fecha, duración, etc.

class Pregunta(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    # Otros campos necesarios para la pregunta, como tipo de respuesta, etc.

class Alternativa(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)
    # Otros campos necesarios para la alternativa, como valor, etc.

class Nota(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    alumno = models.CharField(max_length=255)
    nota = models.FloatField()
    # Otros campos necesarios para la nota del alumno, como fecha, etc.