from django.urls import path
from .views import ListaProductosView, DetalleProductoView

app_name = 'productos'

urlpatterns = [
    path('productos/', ListaProductosView.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', DetalleProductoView.as_view(), name='detalle_producto'),
   
]
