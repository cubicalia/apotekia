from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    first_name = models.CharField(_('First title'), max_length=255, blank=True)
    last_name = models.CharField(_('Last title'), max_length=255, blank=True)
    date_of_birth = models.DateField(_('Date of birth'), blank=True, null=True)
    id_number = models.CharField(_('ID'), max_length=12, blank=True)
    email = models.EmailField(_('Email'), blank=True)
    address = models.TextField(_('Address'), blank=True)
    city = models.CharField(_('City'), max_length=128, blank=True)
    country = models.CharField(_('Country'), max_length=128, blank=True, default='Morocco')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name



