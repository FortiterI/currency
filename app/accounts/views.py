from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import SignUpForm
from accounts.models import User


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    template_name = 'my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name'
    )

    def get_object(self, queryset=None):
        return self.request.user


class SignUp(CreateView):
    queryset = User.objects.all()
    template_name = "signup.html"
    success_url = reverse_lazy("index")
    form_class = SignUpForm
