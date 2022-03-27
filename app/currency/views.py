from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm


def show_all_contactus_records(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contact_us_list.html', context={"contacts": contacts})


class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = "rate.html"


class RateCreate(CreateView):
    model = Rate
    template_name = "create.html"
    form_class = RateForm
    success_url = reverse_lazy("currency:rate_list")


class RateDetail(DetailView):
    model = Rate
    template_name = "rate_detail.html"


class RateUpdate(UpdateView):
    model = Rate
    template_name = "update.html"
    form_class = RateForm
    success_url = reverse_lazy("currency:rate_list")


class RateDelete(DeleteView):
    model = Rate
    template_name = "delete.html"
    success_url = reverse_lazy("currency:rate_list")


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
