import os
import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify


def cryptocurrency_logo_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.symbol)}-{uuid.uuid4()}{extension}"

    return os.path.join("logos/", filename)


class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=16)
    current_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    market_cap = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    rank = models.PositiveIntegerField(default=0, blank=True)
    image = models.ImageField(
        upload_to=cryptocurrency_logo_file_path, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        """Save the cryptocurrency after making symbol uppercase."""
        if self.symbol:
            self.symbol = self.symbol.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        """Meta class for ordering cryptocurrencies by rank."""
        return self.name

    class Meta:
        ordering = ["rank"]


@receiver(pre_delete, sender=Cryptocurrency)
def delete_image_file(sender, instance, **kwargs):
    """Delete the image file when deleting the object."""

    if instance.image:
        instance.image.delete(False)
