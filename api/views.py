from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.core import CurrencyBackend
from api.models import Currency
from api.serializers import CurrencySerializer


@api_view(['GET'])
def get_all_currencies(request):
    query_results = Currency.objects.all()
    data = [CurrencySerializer(currency).data for currency in query_results]
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def get_exchange_rate(request):
    """get currency results"""
    base_currency = request.data['base_currency']
    amount = request.data['amount']
    target_currency = request.data['target_currency']
    currency_backend = CurrencyBackend()
    rate = currency_backend.get_conversion_rate(base_currency, target_currency)
    if rate["status"] == "success":
        response = {
            "base_currency": base_currency,
            "target_currency": target_currency,
            "amount": (rate["rate"] * amount),
            "rate": rate["rate"]
            }
    else:
        response = {"error": rate["rate"]}
    return Response(response)
