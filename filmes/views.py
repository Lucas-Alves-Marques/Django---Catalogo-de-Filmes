from django.shortcuts import render,redirect,get_object_or_404
from .models import Filme
from .forms import FilmeForm


def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista.html', {'filmes': filmes})

def criar_filmes(resquest):
    if resquest.method == 'POST':
        form = FilmeForm(resquest.POST, resquest.FILES)
        if form.is_valid():
            form.save()
            return render('lista_filmes')
    else:
        form = FilmeForm()
        return render(resquest, 'filmes/form_filme.html',{'form': form})

def atualizar_filmes(resquest, pk):
    filme= get_object_or_404(Filme, pk=pk)
    if resquest.method == 'POST':
        form = FilmeForm(resquest.POST, resquest.FILES, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')
    else:
        form = FilmeForm(instance=filme)
    return render(request,'filmes/form_filme.html', {'form': form})

def deletar_filme(resquest, pk):
    filme =get_object_or_404(Filme, pk=pk)
    if resquest.method == 'POST':
        filme.delete()
        return redirect('lista_filme')
    return render(resquest, 'filmes/confirmar_exclusao.html', {'filme': filme})

