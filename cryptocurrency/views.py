from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from cryptocurrency.models import Cryptocurrency
from cryptocurrency.serializers import CryptocurrencyListSerializer


class CryptocurrencyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class CryptocurrencyListView(ListAPIView):
    serializer_class = CryptocurrencyListSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cryptocurrency/cryptocurrency_list.html"
    pagination_class = CryptocurrencyPagination

    def get(self, request):
        queryset = Cryptocurrency.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serialized_data = self.serializer_class(
            paginated_queryset, many=True
        ).data
        return Response(
            {
                "cryptocurrency_list": serialized_data,
                "page_obj": self.paginator.page,
            }
        )


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
