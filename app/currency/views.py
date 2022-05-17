from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.http.request import QueryDict
from currency.filters import RateFilter
from currency.models import ContactUs, Rate, Source
from currency.forms import RateForm, SourceForm
from currency.tasks import send_email


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = "contactus_create.html"
    success_url = reverse_lazy("index")
    fields = (
        "name",
        "reply_to",
        "subject",
        "body",
    )

    def form_valid(self, form):
        response = super().form_valid(form)
        send_email.delay(self.object.name, self.object.reply_to, self.object.subject, self.object.body)
        return response


class RateList(FilterView):
    queryset = Rate.objects.all().order_by('-id').select_related('source')
    template_name = "rate.html"
    paginate_by = 5
    filterset_class = RateFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query_params = QueryDict(mutable=True)

        for key, value in self.request.GET.items():
            if key != 'page':
                query_params[key] = value

        context['filter_params'] = query_params.urlencode()
        return context


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
    template_name = "source_update.html"
    form_class = SourceForm
    success_url = reverse_lazy("currency:source_list")


class SourceDelete(DeleteView):
    model = Source
    template_name = "delete.html"
    success_url = reverse_lazy("currency:source_list")
