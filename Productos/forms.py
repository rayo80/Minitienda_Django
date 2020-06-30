from django import forms
from .models import categoria ,subcategoria,producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = ('titulo',)

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = subcategoria
        fields = ('titulo','categoria_id')      


class ProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ('categoria_id','sub_categoria_id','titulo','usuario_id','descripcion','precio','foto')   
