from django.dispatch import Signal, receiver
from django.utils import timezone
from .models import User


login_signal = Signal(providing_args=['email'])


@receiver(login_signal)
def save_last_login_datetime(sender, **kwargs):
    user = User.objects.get(email=kwargs.get('email'))
    user.last_login = timezone.now()
    user.save()
