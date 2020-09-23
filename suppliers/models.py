from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_default_currency


class Supplier(models.Model):
    name = models.CharField(_('Supplier name'), max_length=128)
    identification = models.CharField(_('Identification number'), max_length=128, null=True, blank=True)

    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), null=True, blank=True)

    class Meta:
        app_label = 'suppliers'
        verbose_name = _('Supplier')
        verbose_name_plural = _('Suppliers')

    def __str__(self):
        return self.name
