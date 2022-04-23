from django.db import models
import currency.model_choises as mch


class ContactUs(models.Model):
    created = models.TimeField(auto_now_add=True, )
    name = models.CharField(max_length=64)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=128)
    body = models.CharField(max_length=1024, default=" ")
    raw_content = models.TextField()


class Source(models.Model):
    name = models.CharField(max_length=32)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Rate(models.Model):
    currency_type = models.CharField(max_length=6, choices=mch.RateType.choices)
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
