from django.shortcuts import render, get_object_or_404
from .models import Category, Post

# Create your views here.
# def blog(request):
#     return render(request, 'blog/blog.html')

def blog (request):
    # categories = Category.objects.all()
    posts = Post.objects.all() #Esto permite que se accedan a los servicios de la bd
    return render(request, 'blog/blog.html',{'posts':posts})

def category (request, category_id):
    #! ⇊ Logica generica ⇊ 
    #* category = Category.objects.get(id=category_id)  El '.get()' busca solamente 1 campo. Buscara la categoria que tiene ese id.
    # return render(request,'blog/category.html',{'category':category}) # Diccionario de contexto.

    #! ⇊ Logica con el 404 ⇊
    # category = get_object_or_404(Category, id=category_id) # Muestra error 404 si no encuentra el id.
    # posts = Post.objects.filter(categories = category) # El '.filter' filtrara los post que posean el category_id
    # return render(request,'blog/category.html',{
    #                                             'category':category,
    #                                             'posts':posts
    #                                             })

    #! ⇊ Otra forma de hacerlo ⇊ (No se le pasa el post, se busca con la relacion inversa)
    category = get_object_or_404(Category, id=category_id)
    return render(request,'blog/category.html',{'category':category,})