from django import forms
from currency.models import Rate, Source


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('currency_type', 'buy', 'sale', 'source')


class SourceForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ('name', 'url', 'logo')
