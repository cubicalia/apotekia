from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_default_currency


class Supplier(models.Model):
    name = models.CharField(_('Supplier name'), max_length=128)
    identification = models.CharField(_('Identification number'), max_length=128, null=True, blank=True)

    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), null=True, blank=True, auto_now=True)

    phone = models.CharField(_('Phone'), max_length=128, null=True, blank=True)

    address_line_1 = models.TextField(_('Address line 1'), blank=True, null=True)
    address_line_2 = models.TextField(_('Address line 2'), blank=True, null=True)
    postal_code = models.CharField(_('Postal code'), max_length=50, null=True, blank=True)

    city = models.CharField(_('City'), max_length=128, null=True, blank=True)
    country = models.CharField(_('Country'), max_length=128, null=True, blank=True)

    description = models.TextField(_('Description'), blank=True, null=True)

    class Meta:
        app_label = 'suppliers'
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __str__(self):
        return self.name
