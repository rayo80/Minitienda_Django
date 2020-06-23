from django.shortcuts import render
from django.views.generic import TemplateView
from .models import producto

# Create your views here.

class productoView(TemplateView):
    template_name = "productos/index.html"
    
    def get_context_data(self, **kwargs):
        kwargs['productos'] = producto.objects.all()
        return kwargs





