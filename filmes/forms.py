from django import forms
from .models import Filme
from django.core.exceptions import ValidationError
from datetime import date

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'descricao', 'ano', 'genero', 'capa']
        labels = {
            'titulo': 'Título do Filme',
            'descricao': 'Sinopse / Descrição',
            'ano': 'Ano de Lançamento',
            'genero': 'Gênero',
            'capa': 'URL da Capa (Link da Imagem)'
        }
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 2:
            raise ValidationError("O título deve ter pelo menos 2 caracteres.")
        return titulo

    def clean_descricao(self):
        descricao = self.cleaned_data.get('descricao')
        if len(descricao) < 2:
            raise ValidationError("A descrição deve ter pelo menos 2 caracteres.")
        return descricao

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        ano_atual = date.today().year

        if ano < 1895:
             raise ValidationError("O ano não pode ser anterior ao nascimento do cinema (1895).")
        if ano > ano_atual + 5:
            raise ValidationError(f"O ano não pode ser superior a {ano_atual + 5}.")
        
        return ano

    def clean_genero(self):
        genero = self.cleaned_data.get('genero')
        if len(genero) < 2:
            raise ValidationError("O gênero deve ter pelo menos 2 caracteres.")
        return genero

    def clean_capa(self):
        capa = self.cleaned_data.get('capa')
        if not capa:
            raise ValidationError("A URL da capa (link da imagem) é obrigatória.")
        return capa