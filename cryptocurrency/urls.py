from django.urls import path

from .views import CryptocurrencyListView, CryptocurrencyRetrieveView

urlpatterns = [
    path(
        "",
        CryptocurrencyListView.as_view(),
        name="cryptocurrency_list",
    ),
    path(
        "<str:name>/",
        CryptocurrencyRetrieveView.as_view(),
        name="cryptocurrency_detail",
    ),
]

app_name = "cryptocurrency"
