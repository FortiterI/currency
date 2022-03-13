from django.http import HttpResponse
from currency.models import ContactUs


def show_all_contactus_records(request):
    contacts = []
    for contact in ContactUs.objects.all():
        contacts.append((contact.id, contact.email_from, contact.subject, contact.message))
    return HttpResponse(str(contacts))
