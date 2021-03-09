import json

import requests
from rest_framework.response import Response

from api.models import Currency, CurrencyRate
from api.serializers import CurrencySerializer


def get_all_currencies(request):
    query = Currency.objects.all()
    return Response(CurrencySerializer(query).data)


def get_exchange_rate(request):
    """get currency results"""
    currency_code = request.data['currency_code']
    amount = request.data['currency_code']
    target_currency = request.data['target_currency']
    try:
        exchange = CurrencyRate.objects.get(currency_code=currency_code)
        rate = json.loads(exchange.conversion_rates)[target_currency]
    except CurrencyRate.DoesNotExist:
        api_key = "2df1cc4b03d460090f63238c"
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency_code}"
        exchange = requests.get(url)
        if exchange["result"] == "success":
            CurrencyRate.objects.create(currency_code=exchange["base_code"],
                                        conversion_rates=exchange["conversion_rates"])
            rate = exchange["conversion_rates"]["target_currency"]
        else:
            print(exchange["error-type"])

    response = {
        "base_currency": currency_code,
        "target_currency": target_currency,
        "amount": (rate * amount),
        "rate": rate,
        }
    return Response(response)
