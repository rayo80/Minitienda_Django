from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


# Create your models here

class usuario(AbstractUser):
    email= models.EmailField( unique=True)
    celular = PhoneNumberField()
    foto = models.ImageField( upload_to='profile', null=True, blank=True)
    descripcion = models.TextField(max_length=1000,blank=True,null=True)
    

