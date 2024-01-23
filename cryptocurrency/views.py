from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from cryptocurrency.models import Cryptocurrency
from cryptocurrency.serializers import CryptocurrencyListSerializer


class CryptocurrencyListView(ListAPIView):
    serializer_class = CryptocurrencyListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cryptocurrency/cryptocurrency_list.html"

    def get(self, request):
        queryset = Cryptocurrency.objects.all()
        serialized_data = self.serializer_class(queryset, many=True).data
        return Response({"cryptocurrency_list": serialized_data})


class CryptocurrencyRetrieveView(RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cryptocurrency/cryptocurrency_detail.html"
    lookup_field = "name"

    def get(self, request, name):
        cryptocurrency = get_object_or_404(Cryptocurrency, name=name)
        serializer = CryptocurrencyListSerializer(cryptocurrency)
        return Response(
            {"serializer": serializer, "cryptocurrency": cryptocurrency}
        )
