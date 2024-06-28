import mercadopago
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PaymentsWithMercadoPagoView(APIView):
    def post(self, request):
        mercadopage_skd = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

        preference_data = {
            "items": [
                {
                    "title": request.data.get("title"),
                    "quantity": int(request.data.get("quantity")),
                    "currency_id": "PEN",
                    "unit_price": float(request.data.get("unit_price"))
                }
            ],
            # estas url son a las que nos va a redirigir despues de hacer el pago
            "back_urls": {
                "success": "http://localhost:5173/?status=success",
                "failure": "http://localhost:5173/?status=failure",
                "pending": "http://localhost:5173/?status=pending",
            },
            # para que cuando termine de hacer el pago vuelva inmediatamente a una de las 3 opcions que existen en back_url
            "auto_return": "approved"
        }

        preference_response = mercadopage_skd.preference().create(preference_data)
        print(preference_response)
        preference_id = preference_response["response"]

        return Response({
            "preference_id": preference_id
        }, status.HTTP_201_CREATED)
