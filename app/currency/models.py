from django.db import models
from django.templatetags.static import static

import currency.model_choises as mch


def upload_logo(instance, filename: str) -> str:
    return f'source id:{instance.id}/logos/{filename}'


class ContactUs(models.Model):
    created = models.TimeField(auto_now_add=True, )
    name = models.CharField(max_length=64)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024, default=" ")
    raw_content = models.TextField()


class Source(models.Model):
    name = models.CharField(max_length=32)
    code_name = models.PositiveIntegerField(choices=mch.SourceCodeName.choices, unique=True )
    url = models.URLField(max_length=200)
    logo = models.FileField(upload_to=upload_logo, default=None, null=True, blank=True)

    def __str__(self):
        return self.name

    def logo_url(self):

        if self.logo:
            return self.logo.url

        return static('img/logo_bank.png')


class Rate(models.Model):
    currency_type = models.CharField(max_length=8, choices=mch.RateType.choices)
    base_type = models.CharField(max_length=8, choices=mch.RateType.choices, default=mch.RateType.UAH)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
