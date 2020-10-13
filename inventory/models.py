from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_default_currency


class WareHouse(models.Model):
    """
    This class manages the warehouses, Users can sell from one warehouse at a time,
    this means that each user has to select, or admin can assign warehouses to each user.
    If a User or Admin wants to change the POS warehouse, he can do it from the settings.
    """
    name = models.CharField(_('Location name'), max_length=128)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Warehouse")
        verbose_name_plural = _("Warehouses")

    def __str__(self):
        return self.name

    def warehouse_potential_value(self):
        pass

    def warehouse_cost_value(self):
        pass


class InventoryLocation(models.Model):
    """
    Inventory Locations are just for warehouse navigation purposes,
    so users can easily locate stock records inside a warehouse.
    """
    warehouse = models.ForeignKey('inventory.WareHouse', on_delete=models.PROTECT)
    name = models.CharField(_('Location name'), max_length=128)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Inventory Location")
        verbose_name_plural = _("Inventory Locations")

    def __str__(self):
        return self.name


class StockRecord(models.Model):
    """
    Each article purchased or allocated in the warehouse has its unique stock record,
    this informs of its purchase price at the moment, its tax rate, etc.
    """
    location = models.ForeignKey('inventory.InventoryLocation', on_delete=models.PROTECT)
    product = models.ForeignKey('catalog.Product', on_delete=models.PROTECT)
    purchase_price_excl_tax = models.DecimalField(_('Purchase price'),
                                                  max_digits=10,
                                                  decimal_places=2)
    tax_rate = models.DecimalField(_('Tax Rate'),
                                   default=20.0,
                                   max_digits=5,
                                   decimal_places=2)
    selling_price_excl_tax = models.DecimalField(_('Purchase price'),
                                                 max_digits=10,
                                                 decimal_places=2)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Stock Record")
        verbose_name_plural = _("Stock Records")

    def __str__(self):
        return str(self.id)


class InventoryEntry(models.Model):
    """
    The inventory entry creates stock records in the defined location for a warehouse
    """
    location = models.ForeignKey('inventory.InventoryLocation',
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True
                                 )
    product = models.ForeignKey('catalog.Product', on_delete=models.PROTECT)
    qty = models.IntegerField(_('Entry quantity'), default=1)
    date = models.DateTimeField(_('Date & Time'), auto_now=True)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Inventory Entry")
        verbose_name_plural = _("Inventory Entries")

    def __str__(self):
        return str(self.id) + '->' + \
               str(self.location) + ' in ' + \
               str(self.location.warehouse) + '|' + \
               str(self.product) + '--' + str(self.qty)
