
from django.views.generic import ListView, DetailView
from .models import Producto
from django.shortcuts import render
class ListaProductosView(ListView):
    model = Producto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'

class DetalleProductoView(DetailView):
    model = Producto
    template_name = 'productos/detalle_producto.html'
    context_object_name = 'producto'
# En views.py



def index(request):
    productos = Producto.objects.all()
    return render(request, 'base.html', {'productos': productos})
