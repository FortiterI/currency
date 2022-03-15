from django.db import models


class ContactUs(models.Model):
    email_from = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=400)


class Rate(models.Model):
    currency_type = models.CharField(max_length=6)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField()
    source = models.CharField(max_length=32)
