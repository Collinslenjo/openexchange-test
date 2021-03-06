from rest_framework import serializers

from api.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    """CurrencySerializer"""
    class Meta:
        model = Currency
        fields = "__all__"
