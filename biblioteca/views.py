from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Autor, Livro

def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autor_list.html', {'autores': autores})


def autor_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        nacionalidade = request.POST.get('nacionalidade')
        data_nascimento = request.POST.get('data_nascimento')
        biografia = request.POST.get('biografia')
        
        Autor.objects.create(
            nome=nome,
            nacionalidade=nacionalidade,
            data_nascimento=data_nascimento,
            biografia=biografia
        )
        return redirect('autor_list')
    
    return render(request, 'biblioteca/autor_form.html')


def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    
    if request.method == 'POST':
        autor.nome = request.POST.get('nome')
        autor.nacionalidade = request.POST.get('nacionalidade')
        autor.data_nascimento = request.POST.get('data_nascimento')
        autor.biografia = request.POST.get('biografia')
        autor.save()
        return redirect('autor_list')
    
    return render(request, 'biblioteca/autor_form.html', {'autor': autor})


def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    
    if request.method == 'POST':
        autor.delete()
        return redirect('autor_list')
    
    return render(request, 'biblioteca/autor_confirm_delete.html', {'autor': autor})

def livro_list(request):
    livros = Livro.objects.all().select_related('autor')
    return render(request, 'biblioteca/livro_list.html', {'livros': livros})


def livro_create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor_id = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        genero = request.POST.get('genero')
        ano_publicacao = request.POST.get('ano_publicacao')
        numero_paginas = request.POST.get('numero_paginas')
        editora = request.POST.get('editora')
        sinopse = request.POST.get('sinopse')
        
        Livro.objects.create(
            titulo=titulo,
            autor_id=autor_id,
            isbn=isbn,
            genero=genero,
            ano_publicacao=ano_publicacao,
            numero_paginas=numero_paginas,
            editora=editora,
            sinopse=sinopse
        )
        return redirect('livro_list')
    
    autores = Autor.objects.all()
    generos = Livro.GENEROS
    return render(request, 'biblioteca/livro_form.html', {
        'autores': autores,
        'generos': generos
    })


def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if request.method == 'POST':
        livro.titulo = request.POST.get('titulo')
        livro.autor_id = request.POST.get('autor')
        livro.isbn = request.POST.get('isbn')
        livro.genero = request.POST.get('genero')
        livro.ano_publicacao = request.POST.get('ano_publicacao')
        livro.numero_paginas = request.POST.get('numero_paginas')
        livro.editora = request.POST.get('editora')
        livro.sinopse = request.POST.get('sinopse')
        livro.save()
        return redirect('livro_list')
    
    autores = Autor.objects.all()
    generos = Livro.GENEROS
    return render(request, 'biblioteca/livro_form.html', {
        'livro': livro,
        'autores': autores,
        'generos': generos
    })


def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_list')
    
    return render(request, 'biblioteca/livro_confirm_delete.html', {'livro': livro})
