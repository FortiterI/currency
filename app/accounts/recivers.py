from accounts.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def pre_save_last_name(sender, instance, **kwargs):
    if instance.last_name:
        instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=User)
def pre_save_first_name(sender, instance, **kwargs):
    if instance.first_name:
        instance.first_name = instance.first_name.capitalize()


@receiver(pre_save, sender=User)
def pre_save_phone(sender, instance, **kwargs):
    if instance.phone:
        if not instance.phone.isdigit():
            phone_list = []
            for i in instance.phone:
                if i.isdigit():
                    phone_list += i
            instance.phone = ''.join(phone_list)
        if instance.phone.startswith('380'):
            instance.phone = instance.phone.replace('380', '0')


@receiver(pre_save, sender=User)
def pre_save_email_lowercase(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(post_save, sender=User)
def post_save_profile(sender, instance, **kwargs):
    pass
