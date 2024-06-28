from django.urls import path
from .views import PaymentsWithMercadoPagoView

urlpatterns = [
    path(r'create-preference/', PaymentsWithMercadoPagoView.as_view(),
         name='mercadopago-create-preference')
]
