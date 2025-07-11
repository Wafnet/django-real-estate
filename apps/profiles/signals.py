import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile
from real_estate.settings.base import AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a Profile instance when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    """
    Save the Profile instance when the User is saved.
    """
    instance.profile.save()
    logger.info(f"{instance.username}'s profile has been created successfully.")
