# importar nuestra clase viewset
from .views import ProductViewSet, CategoryViewSet
# importar el router de DRF (Django Rest Framework)
from rest_framework.routers import DefaultRouter

# crear una instancia de DefaultRouter
router = DefaultRouter(trailing_slash='/')
# agregar una ruta usando router
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
