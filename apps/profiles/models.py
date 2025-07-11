from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(
        verbose_name=_("phone Number"), max_length=20, default="+254724238891"
    )
    about_me = models.TextField(
        verbose_name=_("about me"), default="Say something about yourself"
    )
    license = models.CharField(
        verbose_name=_("Real Estate License"), max_length=20, blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="default_profile_photo.png"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(verbose_name=_("Country"), default="KE")
    city = models.CharField(
        verbose_name=_("City"), max_length=100, default="Nairobi", blank=True, null=True
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Is Buyer"),
        default=False,
        help_text=_("Are you looking to buy a Property?"),
    )
    is_seller = models.BooleanField(
        verbose_name=_("Is Seller"),
        default=False,
        help_text=_("Are you looking to sell a Property?"),
    )
    is_agent = models.BooleanField(
        verbose_name=_("Is Agent"),
        default=False,
        help_text=_("Are you a Real Estate Agent?"),
    )
    top_agent = models.BooleanField(
        verbose_name=_("Top Agent"),
        default=False,
    )
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(
        verbose_name=_("Number of Reviews"), default=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
