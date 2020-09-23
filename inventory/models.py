from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_default_currency


class InventoryLocation(models.Model):
    name = models.CharField(_('Location name'), max_length=128)

    def __str__(self):
        return 'Location: ' + self.name


# class InventoryPurchaseOrderEntry(models.Model):
#     product = models.ForeignKey(
#         'catalog.Product',
#         on_delete=models.CASCADE,
#         related_name="stockrecords",
#         verbose_name=_("Product"))
#
#     location = models.ForeignKey(
#         'inventory.InventoryLocation',
#         on_delete=models.CASCADE,
#         related_name="stockrecords",
#         verbose_name=_("Location"))
#
#     order = models.ForeignKey(
#         'purchases.PurchaseOrder',
#         on_delete=models.CASCADE,
#         related_name="stockrecords",
#         verbose_name=_("Order"),
#         blank=True, null=True)
#
#     price_currency = models.CharField(
#         _("Currency"), max_length=12, default=get_default_currency)
#     price_unit_in = models.DecimalField(
#         _("Price"), decimal_places=2, max_digits=12,
#         blank=True, null=True)
#     price_unit_out = models.DecimalField(
#         _("Price"), decimal_places=2, max_digits=12,
#         blank=True, null=True)
#     transaction_qty = models.PositiveIntegerField(
#         _("Number in stock"), blank=True, null=True)
#
#     date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
#     date_updated = models.DateTimeField(_("Date updated"), auto_now=True,
#                                         db_index=True)
#
#     class Meta:
#         app_label = 'inventory'
#         verbose_name = _("Inventory Entry from PO")
#         verbose_name_plural = _("SInventory entries from POs")POs


class InventoryCustomerReturnEntry(models.Model):
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name="stockrecords",
        verbose_name=_("Product"))

    location = models.ForeignKey(
        'inventory.InventoryLocation',
        on_delete=models.CASCADE,
        related_name="stockrecords",
        verbose_name=_("Location"))

    order = models.ForeignKey(
        'returns.OrderReturn',
        on_delete=models.CASCADE,
        related_name="stockrecords",
        verbose_name=_("Order"),
        blank=True, null=True)

    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date updated"), auto_now=True,
                                        db_index=True)

    class Meta:
        app_label = 'inventory'
        verbose_name = _("Customer Return Order")
        verbose_name_plural = _("Customer Return Orders")


class InventoryCustomerPurchaseExit(models.Model):
    pass


class InventorySupplierReturnOrder(models.Model):
    pass



