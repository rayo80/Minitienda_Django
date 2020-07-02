from django.conf.urls import url
from django.urls import path
from .views import productoView ,ProductoDetallado,FormularioCategoriaView,FormularioSubcategoriaView,FormularioProductoView,ProductoListado






urlpatterns = [
     path('',productoView.as_view(),name='index'),
     #en vez de int se usa slug
     path('<slug:slug>',ProductoDetallado.as_view(),name='producto_detallado'), 
     #url para el formulario
     path('formulario_cat/',FormularioCategoriaView.as_view(),name='formulario'),
     #url para formulario subcategoria
     path('formulario_subcat/',FormularioSubcategoriaView.as_view(),name='formulario_subcategoria'),
     #url para productos
     path('formulario_product/',FormularioProductoView.as_view(),name='formulario_producto'),


     path('listado/',ProductoListado.as_view(),name='enlistado'),
]



