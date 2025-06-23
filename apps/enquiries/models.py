from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

# Create your models here.
class Enquiry(TimeStampedUUIDModel):
    name = models.CharField(_("Your Name"), max_length=180)
    phone_number = PhoneNumberField(_("Your Phone Number"), max_length=20, default="+250724238891")
    email = models.EmailField(_("Email"))
    subject = models.CharField(_("Subject"), max_length=100)
    message = models.TextField(_("Message"))

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Enquiries"
