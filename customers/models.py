from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from django.core import exceptions


class Customer(models.Model):
    MR, MISS, MRS, MS, DR = ('Mr', 'Miss', 'Mrs', 'Ms', 'Dr')
    TITLE_CHOICES = (
        (MR, _("Mr")),
        (MISS, _("Miss")),
        (MRS, _("Mrs")),
        (MS, _("Ms")),
        (DR, _("Dr")),
    )
    title = models.CharField(pgettext_lazy("Treatment Pronouns for the customer", "Title"),
                             max_length=64, choices=TITLE_CHOICES, blank=True)
    first_name = models.CharField(_('First name'), max_length=255, blank=True)
    last_name = models.CharField(_('Last name'), max_length=255, blank=True)
    date_of_birth = models.DateField(_('Date of birth'), blank=True, null=True)
    id_number = models.CharField(_('ID'), max_length=12, blank=True)
    email = models.EmailField(_('Email'), blank=True)
    address = models.ForeignKey('address.Address',
                                null=True, blank=True,
                                verbose_name=_("Address"),
                                on_delete=models.CASCADE)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    @property
    def salutation(self):
        """
        Name (including title)
        """
        return self.join_fields(
            ('title', 'first_name', 'last_name'),
            separator=" ")

    def join_fields(self, fields, separator=", "):
        """
        Join a sequence of fields using the specified separator
        """
        field_values = self.get_field_values(fields)
        return separator.join(filter(bool, field_values))

    def get_field_values(self, fields):
        field_values = []
        for field in fields:
            # Title is special case
            if field == 'title':
                value = self.get_title_display()
            elif field == 'country':
                try:
                    value = self.address.country.printable_name
                except exceptions.ObjectDoesNotExist:
                    value = ''
            elif field == 'salutation':
                value = self.salutation
            else:
                value = getattr(self, field)
            field_values.append(value)
        return field_values
