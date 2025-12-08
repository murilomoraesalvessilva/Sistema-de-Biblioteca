from django.urls import path
from . import views

urlpatterns = [
    # URLs de Autores
    path('', views.autor_list, name='autor_list'),
    path('autores/', views.autor_list, name='autor_list'),
    path('autores/novo/', views.autor_create, name='autor_create'),
    path('autores/<int:pk>/', views.autor_detail, name='autor_detail'),
    path('autores/<int:pk>/editar/', views.autor_update, name='autor_update'),
    path('autores/<int:pk>/excluir/', views.autor_delete, name='autor_delete'),
    
    # URLs de Livros
    path('livros/', views.livro_list, name='livro_list'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/<int:pk>/editar/', views.livro_update, name='livro_update'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro_delete'),
]