from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_default_currency


class InventoryLocation(models.Model):
    name = models.CharField(_('Location name'), max_length=128)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Inventory Location")
        verbose_name_plural = _("Inventory Locations")

    def __str__(self):
        return 'Location: ' + self.name


class InventoryTable(models.Model):
    location = models.ForeignKey('inventory.InventoryLocation', on_delete=models.PROTECT)
    date = models.DateTimeField(_('Date and time of entries'))

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Inventory Table Entry")
        verbose_name_plural = _("Inventory Table Entries")

    def __str__(self):
        return self.location, ': ', self.date, ''


class InventoryEntry(models.Model):
    table = models.ForeignKey('inventory.InventoryTable', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', on_delete=models.PROTECT)
    qty = models.IntegerField(_('Initial count'), default=0)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Inventory Table EntriesO")
        verbose_name_plural = _("Inventory Table Entries")

    def __str__(self):
        return self.table, ': ', self.product, '', str(self.qty)