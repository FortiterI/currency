from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from settings import settings as st


@shared_task()
def send_activation_email(username: str, email: str):
    subject = "Sing Up"
    body = f"""
                Activation Link:
                {st.HTTP_SCHEMA}://{st.DOMAIN}{reverse('accounts:activate-user', args=[username])}
            """
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
