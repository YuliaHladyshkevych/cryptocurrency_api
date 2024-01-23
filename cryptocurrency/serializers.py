from rest_framework import serializers

from cryptocurrency.models import Cryptocurrency


class CryptocurrencyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = "__all__"
