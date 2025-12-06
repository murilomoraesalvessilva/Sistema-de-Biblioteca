from django.contrib import admin
from .models import Autor, Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nacionalidade', 'data_nascimento', 'quantidade_livros', 'data_cadastro']
    search_fields = ['nome', 'nacionalidade']
    list_filter = ['nacionalidade', 'data_nascimento']
    date_hierarchy = 'data_nascimento'


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'genero', 'ano_publicacao', 'editora', 'isbn']
    search_fields = ['titulo', 'isbn', 'autor__nome']
    list_filter = ['genero', 'ano_publicacao', 'autor']
    date_hierarchy = 'data_cadastro'
    raw_id_fields = ['autor']