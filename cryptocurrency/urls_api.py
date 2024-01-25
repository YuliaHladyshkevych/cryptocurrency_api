from django.urls import path

from .views import CryptocurrencyViewSet

urlpatterns = [
    path(
        "cryptocurrencies/",
        CryptocurrencyViewSet.as_view({"get": "list"}),
        name="cryptocurrency-list-api",
    ),
]

app_name = "cryptocurrency"
