from django.shortcuts import render
from currency.models import ContactUs, Rate


def show_all_contactus_records(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contact_us_list.html', context={"contacts": contacts})


def index(request):
    return render(request, 'index.html')


def rate(request):
    rates = Rate.objects.all()
    return render(request, "rates.html", context={"rates": rates})
