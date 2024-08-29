from django.shortcuts import render
from .models import Curso, Interesse


def home(request):
    return render(request, "home.html")


def sobre(request):
    interesses = Interesse.objects.all()
    return render(request, "sobre.html", {"interesses": interesses})


def cursos(request):
    cursos = Curso.objects.all().order_by("-ano_conclusao")
    return render(request, "cursos.html", {"cursos": cursos})
