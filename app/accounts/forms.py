from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from settings import settings as st
from accounts.models import User


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords should match!')

        return self.cleaned_data

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        cleaned_data = self.cleaned_data

        user = super(SignUpForm, self).save(commit=False)
        user.set_password(cleaned_data['password1'])
        user.is_active = False

        if commit:
            user.save()

        self._send_activation_email(user)

        return user

    def _send_activation_email(self, user):
        subject = "Sing Up"
        body = f"""
                    Activation Link:
                    {st.HTTP_SCHEMA}://{st.DOMAIN}{reverse('accounts:activate-user', args= [user.username])}
                """
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False
        )
