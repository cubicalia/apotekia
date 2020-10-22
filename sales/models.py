from decimal import Decimal as D

from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import gettext_lazy as _

from apotekia.utils import get_default_currency
from customers.models import Customer


class Basket(models.Model):
    employee = models.ForeignKey(
        AUTH_USER_MODEL,
        null=True,
        related_name='sales',
        on_delete=models.CASCADE,
        verbose_name=_("Employee"))

    customer = models.ForeignKey(
        'customers.Customer',
        null=True,
        related_name='sales',
        on_delete=models.PROTECT,
        verbose_name=_("Customer"))

    # Basket statuses
    # - Frozen is for when a basket is in the process of being submitted
    #   and we need to prevent any changes to it.
    OPEN, MERGED, SAVED, FROZEN, SUBMITTED = (
        "Open", "Merged", "Saved", "Frozen", "Submitted")
    STATUS_CHOICES = (
        (OPEN, _("Open - currently active")),
        (MERGED, _("Merged - superceded by another basket")),
        (SAVED, _("Saved - for items to be purchased later")),
        (FROZEN, _("Frozen - the basket cannot be modified")),
        (SUBMITTED, _("Submitted - has been ordered at the checkout")),
    )
    status = models.CharField(
        _("Status"), max_length=128, default=OPEN, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
    date_merged = models.DateTimeField(_("Date merged"), null=True, blank=True)
    date_submitted = models.DateTimeField(_("Date submitted"), null=True,
                                          blank=True)

    class Meta:
        app_label = 'sales'
        verbose_name = _('Basket')
        verbose_name_plural = _('Baskets')

    def __str__(self):
        pk = self.pk
        date_created = self.date_created
        status = self.status

        return str(pk) + str(date_created) + '-' + status


class BasketLine(models.Model):
    line_reference = models.SlugField(
        _("Line Reference"), max_length=128, db_index=True)
    basket = models.ForeignKey(
        'sales.Basket',
        on_delete=models.CASCADE,
        related_name='lines',
        verbose_name=_("Basket"))

    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        related_name='basket_lines',
        verbose_name=_("Product"))

    quantity = models.PositiveIntegerField(_('Quantity'), default=1)
    price_currency = models.CharField(
        _("Currency"), max_length=12, default=get_default_currency)
    price_excl_tax = models.DecimalField(
        _('Price excl. Tax'), decimal_places=2, max_digits=12,
        null=True)
    price_incl_tax = models.DecimalField(
        _('Price incl. Tax'), decimal_places=2, max_digits=12, null=True)

    # Track date of first addition
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True, db_index=True)

    class Meta:
        app_label = 'sales'
        # Enforce sorting by order of creation.
        ordering = ['date_created', 'pk']
        verbose_name = _('Basket line')
        verbose_name_plural = _('Basket lines')

    def __str__(self):
        return 'Line {} of basket: '.format(self.pk) + str(self.basket.pk)


class Sale(models.Model):
    reference = models.SlugField(
        _("Reference"), max_length=128, db_index=True, unique=True)

    basket = models.ForeignKey(
        'sales.Basket',
        on_delete=models.CASCADE,
        related_name='sale',
        verbose_name=_("Basket"))

    payment = models.OneToOneField('payment.Transaction',
                                   on_delete=models.SET_NULL,
                                   related_name='sale',
                                   verbose_name=_('Payment'),
                                   null=True)

    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True, db_index=True)

    class Meta:
        app_label = 'sales'
        # Enforce sorting by order of creation.
        ordering = ['date_created', 'pk']
        verbose_name = _('Sale')
        verbose_name_plural = _('Sales')

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.reference,
                                          self.customer.get_full_name(),
                                          str(self.payment.amount),
                                          self.date_created.strftime('dd-mm-yyyy'))

class CustomerOrder(models.Model):
    number = models.CharField(_("Order number"),
                              max_length=128,
                              db_index=True,
                              unique=True)

    customer = models.ForeignKey(
        'customers.Customer', related_name='orders', null=True, blank=True,
        verbose_name=_("Customer"), on_delete=models.SET_NULL)

    employee = models.ForeignKey(
        AUTH_USER_MODEL, related_name='orders', null=True, blank=True,
        verbose_name=_("Employee"), on_delete=models.SET_NULL)

    # Total price looks like it could be calculated by adding up the
    # prices of the associated lines, but in some circumstances extra
    # order-level charges are added and so we need to store it separately
    currency = models.CharField(
        _("Currency"), max_length=12, default=get_default_currency)
    total_incl_tax = models.DecimalField(
        _("Order total (inc. tax)"), decimal_places=2, max_digits=12)
    total_excl_tax = models.DecimalField(
        _("Order total (excl. tax)"), decimal_places=2, max_digits=12)

    # Order Status
    OPEN, MERGED, SAVED, SHIPPED_PAID_PARTIALLY, SHIPPED_NOT_PAID, SHIPPED_PAID = (
        "Open", "Merged", "Saved", "Shipped and Paid Partially",
        "Shipped and Not paid ", "Shipped and Paid")
    STATUS_CHOICES = (
        (OPEN, _("Open - currently active")),
        (MERGED, _("Merged - superceded by another order")),
        (SAVED, _("Saved - for items to be purchased later")),
        (SHIPPED_NOT_PAID, _("Shipped and Not paid - the order hasn't been paid yet")),
        (SHIPPED_PAID_PARTIALLY, _("Shipped and Paid Partially - Not totally paid")),
        (SHIPPED_PAID, _("Shipped and Paid - Has been paid")),
    )
    status = models.CharField(
        _("Status"), max_length=128, default=OPEN, choices=STATUS_CHOICES)

    date_placed = models.DateTimeField(db_index=True)

    # Shipping charges
    shipping_incl_tax = models.DecimalField(
        _("Shipping charge (inc. tax)"), decimal_places=2, max_digits=12,
        default=0)
    shipping_excl_tax = models.DecimalField(
        _("Shipping charge (excl. tax)"), decimal_places=2, max_digits=12,
        default=0)

    class Meta:
        app_label = 'sales'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return self.number

    @property
    def basket_total_before_discounts_incl_tax(self):
        """
        Return basket total including tax but before discounts are applied
        """
        total = D('0.00')
        for line in self.order_lines.all():
            total += line.line_price_before_discounts_incl_tax
        return total

    @property
    def basket_total_before_discounts_excl_tax(self):
        """
        Return basket total excluding tax but before discounts are applied
        """
        total = D('0.00')
        for line in self.order_lines.all():
            total += line.line_price_before_discounts_excl_tax
        return total


class CustomerOrderLine(models.Model):
    order = models.ForeignKey('sales.CustomerOrder',
                              related_name='order_lines',
                              verbose_name=_("Customer"),
                              on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product',
                                related_name='order_line_product',
                                verbose_name=_("Customer"),
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(_('Quantity'), default=1)

    price_excl_tax = models.DecimalField(
        _('Price excl. Tax'), decimal_places=2, max_digits=12, null=True)
    price_incl_tax = models.DecimalField(
        _('Price incl. Tax'), decimal_places=2, max_digits=12, null=True)

    # Track date of first addition
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True, db_index=True)