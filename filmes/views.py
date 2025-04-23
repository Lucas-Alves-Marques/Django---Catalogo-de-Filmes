from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Filme

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})

