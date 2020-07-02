from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import producto, categoria
from .forms import CategoriaForm, SubcategoriaForm,ProductoForm
from django.core.paginator import Paginator,PageNotAnInteger



tamaño=producto.objects.count()
i=int(tamaño/20)



# Create your views here.

class productoView(TemplateView):
    template_name = "productos/index.html"
    
    
    
    # def listing(request):
    # contact_list = Contact.objects.all()
    # paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    # return render(request, 'list.html', {'page_obj': page_obj})


    #def get(self,request,*args,**kwargs)

    def get_queryset(self):           
        queryset = producto.objects.all()
        return queryset                
    
    def get_context_data(self, **kwargs):
                
        #kwargs['productos'] = self.page_obj
        #kwargs['productos'] = self.get_queryset() 
        kwargs['20productos']= self.get_queryset()[0:20]
        kwargs['40productos']= self.get_queryset()[20:40]


        #paginacion
        paginator=Paginator(self.get_queryset(),3)
        numerototal=paginator.num_pages
        
        page=self.request.GET.get('page',1)#//el 1 es la pagina que se envia por defecto al llamar con el url por defecto de la pagina
        
        print(page)
        
        #page=int(page) #//el valor de page es un numero pero que es mandado como str
        #objetodelapagina=paginator.page(page)
    
        # if page <0:                                     
        #     objetodelapagina=paginator.page(1)    
        #//no se puede hacer esto debido a que el error ya ha ocurrido al mandar un numero negativo
        #//con el nombre de la excepcion empty
        
        try:
            
            objetodelapagina=paginator.page(page)
            page=int(page)
        except PageNotAnInteger:
            page=1
            objetodelapagina=paginator.page(1)
        
          
        

        
        kwargs['productos']=objetodelapagina
        return kwargs










class ProductoListado(ListView):
    template_name = 'productos/enlistado.html'
    model = producto
    paginate_by = 2
    context_object_name = 'productos'



    




class ProductoDetallado(TemplateView):
    template_name = 'productos/productox.html'
    
    def get_context_data(self, **kwargs):
        libro_slug = kwargs.get('slug') #del url recibe que eslug quiere
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
