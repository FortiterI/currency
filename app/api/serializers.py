from rest_framework import serializers
from currency.models import Rate, Source, ContactUs


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'sale',
            'buy',
            'source',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'created',
            'name',
            'reply_to',
            'subject',
            'body',
        )


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'url',
        )


