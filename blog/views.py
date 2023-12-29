from django.shortcuts import render
from django.http import HttpResponseNotFound

from productos.models import Producto
from apps.posts.models import Categoria, Post

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>Página no encontrada</h1>')

def index(request):
    productos = Producto.objects.all() 
    categorias = Categoria.objects.all()
    posts = Post.objects.filter(activo=True).order_by('-publicado')  
    context = {'productos': productos, 'categorias': categorias, 'posts': posts, 'producto':productos}
    
    
    return render(request, 'index.html', context)
