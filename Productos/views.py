from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import producto, categoria,Queja
from .forms import CategoriaForm, SubcategoriaForm,ProductoForm
from django.core.paginator import Paginator,PageNotAnInteger







distintos = Queja.objects.values('producto').distinct() #no queremos quejas de productos repetidos --->traemos el total de productos que tienen quejas
print(distintos)
for com in distintos:
    prod = producto.objects.filter(id = com['producto']).first()
    contador_total = Queja.objects.filter(producto = prod).count()
    





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
        #agrupar automaticamente       
        qonda=producto.objects.order_by('precio')
        #seleccion de grupos de 4 en 4
        paginas=Paginator(qonda,4)
        numero=paginas.num_pages #me da el total de grupos
        

        objetos_pagina=paginas.page(1)
        
        i=0    
        for i in range(numero):
            i=i+1
            kwargs['bloque'+str(i)]=paginas.page(i)

       
            
            



        #paginacion
        paginator=Paginator(self.get_queryset(),3)
        numerototal=paginator.num_pages
        
        page=self.request.GET.get('page',1)#//el 1 es la pagina que se envia por defecto al llamar con el url por defecto de la pagina
        
        
        
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


class AnunciosReportados(TemplateView):
    template_name = 'productos/anuncios_reportados.html'
    
     
    def get_context_data(self, **kwargs):
        complaints =Queja.objects.all()         #traemos todas las quejas que tengamos
        all_products = producto.objects.all() #traemos todos los productos
        distintos = Queja.objects.values('producto').distinct() #no queremos quejas de productos repetidos --->traemos el total de productos que tienen quejas
        print(distintos)
        prod_cont=[]
        for com in distintos:  
            prod = producto.objects.filter(id = com['producto']).first()   #extraer nombre de producto //el primer producto es el model y el segundo es del campo de la queja
            
            contador_total = Queja.objects.filter(producto = prod).count()  #contar cuantas quejas hay por producto //producto en azul se refiere al campo de la base
            contador_sin_revisar = Queja.objects.filter(producto = prod).count() #filtradas por tema(cuenta las quejas que estan sin revisar)
            prod_slug = prod.slug  #extraer el slug de prod
            prod_cont.append((prod,contador_total, contador_sin_revisar, prod_slug))  #guardar la tupla en el array 



        kwargs['20productos']= Queja.objects.all()[0:20]
        kwargs['40productos']= Queja.objects.all()[20:40]
            
        kwargs['prod_cont'] = prod_cont  #esto envia una tupla
        kwargs['complaints'] = complaints
        kwargs['all_products'] = all_products

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
