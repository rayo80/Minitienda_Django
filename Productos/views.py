from django.shortcuts import render
from django.views.generic import TemplateView
from .models import producto

# Create your views here.

class productoView(TemplateView):
    template_name = "productos/index.html"
    
    def get_context_data(self, **kwargs):
        kwargs['productos'] = producto.objects.all()
        return kwargs




class ProductoDetallado(TemplateView):
    template_name = 'productos/productox.html'
    
    def get_context_data(self, **kwargs):
        libro_slug = kwargs.get('slug')
        kwargs['productoyo'] = producto.objects.get(slug=libro_slug)
        return kwargs


