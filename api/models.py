from django.db import models


class Currency(models.Model):
    """All available Currencies"""
    currency_code = models.CharField(max_length=5, unique=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_currencies'

    def __str__(self):
        return f'{self.currency_code}'


class CurrencyRate(models.Model):
    """Conversion Rates"""
    currency_code = models.CharField(max_length=5, unique=True)
    conversion_rates = models.TextField(null=False)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_currency_rates'

    def __str__(self):
        return f'{self.currency_code}'
