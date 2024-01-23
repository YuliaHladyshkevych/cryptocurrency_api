import requests

from cryptocurrency.models import Cryptocurrency
from cryptocurrency_api import settings


def update_crypto_data():
    parameters = {
        "start": "1",
        "limit": "100",
        "convert": "USD",
    }

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": settings.CMC_PRO_API_KEY,
    }

    try:
        response = requests.get(
            settings.CMC_PRO_API_URL, params=parameters, headers=headers
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

    data = response.json()
    cryptocurrencies = []

    for crypto_data in data["data"]:
        name = crypto_data["name"]
        symbol = crypto_data["symbol"]
        current_price = crypto_data["quote"]["USD"]["price"]
        market_cap = crypto_data["quote"]["USD"]["market_cap"]
        rank = crypto_data["cmc_rank"]

        cryptocurrencies.append(
            Cryptocurrency(
                name=name,
                symbol=symbol,
                market_cap=market_cap,
                rank=rank,
                current_price=current_price,
            )
        )

    return cryptocurrencies


def save_cryptocurrencies(cryptocurrencies: list[Cryptocurrency]):
    for cryptocurrency in cryptocurrencies:
        Cryptocurrency.objects.update_or_create(
            name=cryptocurrency.name,
            defaults={
                "symbol": cryptocurrency.symbol,
                "market_cap": cryptocurrency.market_cap,
                "rank": cryptocurrency.rank,
                "current_price": cryptocurrency.current_price,
            },
        )


def sync_cryptocurrencies_with_api():
    cryptocurrency = update_crypto_data()
    save_cryptocurrencies(cryptocurrency)
