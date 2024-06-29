from django.urls import path
from .views import PaymentsWithMercadoPagoView, CustomCreatePaymentView

urlpatterns = [
    path(r'create-preference/', PaymentsWithMercadoPagoView.as_view(),
         name='mercadopago-create-preference'),
    path(r'create-payment/', CustomCreatePaymentView.as_view(),
         name='mercadopago-create-payment')
]
