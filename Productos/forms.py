from django import forms
from .models import categoria ,subcategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = ('titulo',)

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = subcategoria
        fields = ('titulo','categoria_id')        
