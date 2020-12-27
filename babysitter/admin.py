from django.contrib import admin

# Register your models here.
from babysitter.models import Customer

admin.site.register(Customer) #регистрируем нашу модель Customer в админке


