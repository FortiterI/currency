from django.db import models


class ContactUs(models.Model):
    email_from = models.CharField(max_length=64)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=400)
