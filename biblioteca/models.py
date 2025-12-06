from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    nacionalidade = models.CharField(max_length=100, verbose_name="Nacionalidade")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    biografia = models.TextField(blank=True, null=True, verbose_name="Biografia")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']
    
    def __str__(self):
        return self.nome
    
    def quantidade_livros(self):
        return self.livros.count()


class Livro(models.Model):
    GENEROS = [
        ('FIC', 'Ficção'),
        ('NAO', 'Não-Ficção'),
        ('ROM', 'Romance'),
        ('FAN', 'Fantasia'),
        ('POL', 'Policial'),
        ('BIO', 'Biografia'),
        ('TEC', 'Técnico'),
        ('OUT', 'Outros'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título")
    autor = models.ForeignKey(
        Autor, 
        on_delete=models.CASCADE, 
        related_name='livros',
        verbose_name="Autor"
    )
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    genero = models.CharField(max_length=3, choices=GENEROS, verbose_name="Gênero")
    ano_publicacao = models.IntegerField(verbose_name="Ano de Publicação")
    numero_paginas = models.IntegerField(verbose_name="Número de Páginas")
    editora = models.CharField(max_length=100, verbose_name="Editora")
    sinopse = models.TextField(blank=True, null=True, verbose_name="Sinopse")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['titulo']
    
    def __str__(self):
        return f"{self.titulo} - {self.autor.nome}"