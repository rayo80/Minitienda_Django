from django.contrib import admin

# Register your models here.
from .models import categoria
from .models import subcategoria
from .models import producto

from .models import Queja

# Register your models here.
admin.site.register(categoria)
admin.site.register(subcategoria)
admin.site.register(producto)
admin.site.register(Queja)