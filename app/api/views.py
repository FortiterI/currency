from rest_framework import viewsets, generics
from api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
from currency.models import Rate, Source, ContactUs
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)


class SourceView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
