from django.shortcuts import render

from .models import Pregunta, Opcion
# Create your views here.

def index(request):
    lista_pregunta = Pregunta.objects.all()
    context = {
        'preguntas' : lista_pregunta
    }
    return render(request, 'index.html',context)

def resolver(request):
    preguntas = Pregunta.objects.all()
    nota = 0
    for pregunta in preguntas:
        nota = int(request.POST['pregunta_'+str(pregunta.id)])
    
    context = {
        'nota' : nota
    }

    return render(request, 'resultados.html',context)