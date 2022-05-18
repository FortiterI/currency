from rest_framework import serializers
from currency.models import Rate, Source, ContactUs
from currency.tasks import send_email


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'currency_type',
            'sale',
            'buy',
            'source',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        message = ContactUs.objects.create(**validated_data)
        send_email.delay(validated_data.get('name'),
                         validated_data.get('reply_to'),
                         validated_data.get('subject'),
                         validated_data.get('body'),
                         )
        return message

    class Meta:
        model = ContactUs
        fields = (
            'id',
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
