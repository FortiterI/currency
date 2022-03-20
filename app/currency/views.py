from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm


def show_all_contactus_records(request):
    contacts = ContactUs.objects.all()
    return render(request, 'contact_us_list.html', context={"contacts": contacts})


def index(request):
    return render(request, 'index.html')


def rate_list(request):
    rates = Rate.objects.all().order_by("-id")
    return render(request, "rate.html", context={"rates": rates})


def rate_create(request):

    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/rate/list/")
    else:
        form = RateForm()  # empty form
    return render(request, "create.html", context={"form":  form, "model_name": "Rate"})


def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)
    if request.method == "POST":
        form = RateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/rate/list/")
    else:
        form = RateForm(instance=instance)
    return render(request, "update.html", context={"form":  form, "model_name": "Rate"})


def rate_delete(request, pk):
    instance = get_object_or_404(Rate, pk=pk)
    if request.method == "POST":
        instance.delete()
        return HttpResponseRedirect("/rate/list/")
    else:
        return render(request, "delete.html", context={"cont": instance, "model_name": "Rate"})


def source_list(request):
    sources = Source.objects.all()
    return render(request, "source_list.html", context={"sources": sources})


def source_create(request):
    if request.method == "POST":
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/source/list/")
    else:
        form = SourceForm()  # empty form
    return render(request, "create.html", context={"form":  form, "model_name": "Source"})


def source_update(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == "POST":
        form = SourceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/source/list/")
    else:
        form = SourceForm(instance=instance)
    return render(request, "update.html", context={"form":  form, "model_name": "Source"})


def source_delete(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == "POST":
        instance.delete()
        return HttpResponseRedirect("/source/list/")
    else:
        return render(request, "delete.html", context={"cont": instance, "model_name": "Source"})
