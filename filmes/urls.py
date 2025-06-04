from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.lista_filmes, name='lista_filmes'),
    path('new/', views.criar_filmes, name='criar_filmes'),
    path('edit/<int:pk>/', views.atualizar_filmes, name='atualizar_filmes'),
    path('delete/<int:pk>/', views.deletar_filme, name='deletar_filmes')
    
]