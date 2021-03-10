import json

import requests

from api.models import CurrencyRate


class CurrencyBackend:
    @staticmethod
    def get_conversion_rate(base_currency, target_currency):
        """returns the rate or error"""
        try:
            exchange = CurrencyRate.objects.get(currency_code=base_currency)
            try:
                rate = json.loads(exchange.conversion_rates)[f"{target_currency}"]
            except KeyError:
                rate = "Target Currency Does Not Exist"
        except CurrencyRate.DoesNotExist:
            api_key = "2df1cc4b03d460090f63238c"
            exchange = requests.get(
                f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}")\
                .json()
            if exchange["result"] == "success":
                CurrencyRate.objects.create(
                    currency_code=exchange["base_code"],
                    conversion_rates=json.dumps(exchange["conversion_rates"]))
                rate = exchange["conversion_rates"][f"{target_currency}"]
            else:
                rate = exchange["error-type"]

        if type(rate) == str:
            response = {"status": "failed", "rate": rate}
        else:
            response = {"status": "success", "rate": rate}
        return response
