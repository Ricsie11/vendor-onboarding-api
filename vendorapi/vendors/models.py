from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Vendor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField(blank=False, null=False)
    type_of_service = models.CharField(max_length=255, blank=False, null=False)
    years_in_business = models.PositiveIntegerField()
    phone_number = PhoneNumberField(unique=True)
    cac_certificate = models.ImageField(upload_to="documents/cac_certificates/")
    verified_id = models.ImageField(upload_to="documents/verified_ids/")
    proof_of_address = models.ImageField(upload_to="documents/address/")
    is_onboarded = models.BooleanField(default=False)

    def __str__(self):
         return f"Vendor: {self.user.get_full_name() or self.user.username}"
    


    class Meta:
         verbose_name = "Vendor"
         verbose_name_plural = "Vendors"
