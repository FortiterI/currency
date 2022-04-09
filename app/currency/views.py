from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm
from django.conf import settings


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = "Contactus_create.html"
    success_url = reverse_lazy("index")
    fields = (
        "name",
        "reply_to",
        "subject",
        "body",
    )

    def _send_email(self, ):
        recipient = settings.EMAIL_HOST_USER
        subject = "User ContactUs"
        body = f"""
            Request From: {self.object.name}
            Email to reply: {self.object.reply_to}
            Subject: {self.object.subject}
            Body: {self.object.body}
        """
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [recipient],
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        self._send_email()
        return response


class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = "rate.html"


class RateCreate(UserPassesTestMixin, CreateView):
    model = Rate
    template_name = "create.html"
    form_class = RateForm
    success_url = reverse_lazy("currency:rate_list")

    def test_func(self):
        return self.request.user.is_superuser


class RateDetail(DetailView):
    model = Rate
    template_name = "rate_detail.html"


class RateUpdate(UserPassesTestMixin, UpdateView):
    model = Rate
    template_name = "update.html"
    form_class = RateForm
    success_url = reverse_lazy("currency:rate_list")

    def test_func(self):
        return self.request.user.is_superuser


class RateDelete(UserPassesTestMixin, DeleteView):
    model = Rate
    template_name = "delete.html"
    success_url = reverse_lazy("currency:rate_list")

    def test_func(self):
        return self.request.user.is_superuser


class SourceList(ListView):
    model = Source
    template_name = "source_list.html"


class SourceDetail(DetailView):
    model = Source
    template_name = "source_detail.html"


class SourceCreate(CreateView):
    model = Source
    template_name = "create.html"
    form_class = SourceForm
    success_url = reverse_lazy("currency:source_list")


class SourceUpdate(UpdateView):
    model = Source
    template_name = "update.html"
    form_class = SourceForm
    success_url = reverse_lazy("currency:source_list")


class SourceDelete(DeleteView):
    model = Source
    template_name = "delete.html"
    success_url = reverse_lazy("currency:source_list")


def source_delete(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == "POST":
        instance.delete()
        return redirect('currency:source_list')
    else:
        return render(request, "delete.html", context={"cont": instance, "model_name": "Source"})
