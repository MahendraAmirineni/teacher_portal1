from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Teacher

@receiver(post_save, sender=User)
def create_teacher_for_new_user(sender, instance, created, **kwargs):
    if created:  # If a new User is created
        Teacher.objects.create(user=instance)  # Create a Teacher instance for the User

# In apps.py, make sure to connect the signal
# apps.py

from django.apps import AppConfig

class PortalConfig(AppConfig):
    name = 'portal'

    def ready(self):
        import portal.signals  # Ensure the signal is loaded
