from django.shortcuts import render,redirect,get_object_or_404
from .models import Filme
from .forms import FilmeForm

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})

def criar_filmes(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm()
        
    return render(request, 'filmes/form_filme.html', {'form': form})

def atualizar_filmes(request, pk):
    filme= get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request,'filmes/form_filme.html', {'form': form})

def deletar_filme(request, pk):
    filme =get_object_or_404(Filme, pk=pk)
    if request.method == 'POST':
        filme.delete()
        return redirect('lista_filmes')
    return render(request, 'filmes/confirmar_exclusao.html', {'filme': filme})

