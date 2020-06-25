from django import forms
from .models import categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria
        fields = ('titulo',)
