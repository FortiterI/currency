from rest_framework import viewsets, generics

from api.v1.pagination import RatePagination, ContactUsPagination
from api.v1.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from api.v1.throttels import AnonCurrencyThrottle
from currency.models import Rate, Source, ContactUs
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from api.v1.filters import RateFilter, ContactUsFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as rest_framework_filters


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-id')
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        DjangoFilterBackend,
        rest_framework_filters.OrderingFilter
    )
    ordering_fields = ('-id', 'sale', 'buy', )
    throttle_classes = [AnonCurrencyThrottle]


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
    pagination_class = ContactUsPagination
    filterset_class = ContactUsFilter
    filter_backends = (
        DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
        rest_framework_filters.SearchFilter
    )
    ordering_fields = ('name', 'reply_to', 'subject')
    throttle_classes = [AnonCurrencyThrottle]
    search_fields = ['name', 'reply_to']


class SourceView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
