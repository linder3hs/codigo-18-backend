from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    # Permite crear un tupla con los campos que queremos mostrar en el admin
    list_display = ('id', 'name', 'description', 'price', 'stock', 'category')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
