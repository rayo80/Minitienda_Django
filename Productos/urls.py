from django.conf.urls import url
from django.urls import path
from .views import productoView

urlpatterns = [
     path('',productoView.as_view(),name='index'),
]