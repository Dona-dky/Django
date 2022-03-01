from django.contrib import admin

from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
  fields = ['text','date']

admin.site.register(Product)