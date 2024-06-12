from django.http import JsonResponse
from .models import Product


def get_products(request):
    # todos los productos que creamos
    # usando el DJango ORM (Permite interactuar con la base de datos)
    products = Product.objects.all()
    serialize_products = []
    for product in products:
        serialize_products.append({
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'stock': product.stock,
            'category': product.category,
            'is_active': product.is_active,
            'created_at': product.created_at,
            'updated_at': product.updated_at
        })

    return JsonResponse(serialize_products, safe=False)
