from django.conf.urls import url
from django.urls import path
from .views import productoView ,ProductoDetallado




urlpatterns = [
     path('',productoView.as_view(),name='index'),
     #en vez de int se usa slug
     path('<slug:slug>',ProductoDetallado.as_view(),name='producto_detallado'), 
]