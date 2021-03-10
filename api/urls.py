from django.urls import re_path

from api.views import get_exchange_rate, get_all_currencies, home

api_prefix = 'api'

urlpatterns = [
    re_path(r'^', home),
    re_path(fr'^{api_prefix}/currencies', get_all_currencies),
    re_path(fr'^{api_prefix}/currency/convert', get_exchange_rate),

]
