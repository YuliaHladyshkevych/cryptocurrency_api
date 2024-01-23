from rest_framework.generics import ListAPIView

from cryptocurrency.models import Cryptocurrency
from cryptocurrency.serializers import CryptocurrencyListSerializer


class CryptocurrencyListView(ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencyListSerializer
