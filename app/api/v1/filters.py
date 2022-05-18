import django_filters
from currency.models import Rate, ContactUs


class RateFilter(django_filters.FilterSet):
    class Meta:
        model = Rate
        fields = {
            'buy': ('gte', 'lte'),
            'sale': ('gte', 'lte'),
            'currency_type': ('exact',),
        }


class ContactUsFilter(django_filters.FilterSet):
    class Meta:
        model = ContactUs
        fields = {'name': ('exact',),
                  'reply_to': ('exact',),
                  'subject': ('exact',)
                  }
