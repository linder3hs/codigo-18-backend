# importar nuestra clase viewset
from .views import ProductViewSet
# importar el router de DRF (Django Rest Framework)
from rest_framework.routers import DefaultRouter

# crear una instancia de DefaultRouter
router = DefaultRouter()
# agregar una ruta usando router
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
