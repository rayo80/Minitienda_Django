from django.shortcuts import render
from django.views.generic import TemplateView
from .models import producto, categoria
from .forms import CategoriaForm, SubcategoriaForm,ProductoForm

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



#vista del formulario
class FormularioCategoriaView(TemplateView):
    template_name = "productos/formulario_autor.html"
    #CategoriaForm es la clase q hereda de forms 
    def get_context_data(self, **kwargs):
        kwargs['form'] = CategoriaForm   
        return kwargs

    def post(self, request, *args, **kwargs):
        contexto = self.get_context_data(**kwargs)
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()   
        contexto['form'] = form
        return self.render_to_response(contexto)


#vista formulario subcategoria


class FormularioSubcategoriaView(TemplateView):
    template_name = "productos/formulario_subcategoria.html"

    def get_context_data(self, **kwargs):
        kwargs['formita'] = SubcategoriaForm
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
        context['formita'] = form
        return self.render_to_response(context)


class FormularioProductoView(TemplateView):
    template_name = "productos/formulario_productos.html"

    def get_context_data(self, **kwargs):
        kwargs['esteesunvalormanejable'] = ProductoForm
        return kwargs

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        context['esteesunvalormanejable'] = form
        return self.render_to_response(context)
