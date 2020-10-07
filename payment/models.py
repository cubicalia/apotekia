from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia import settings


class PaymentSourceType(models.Model):
    name = models.CharField(_("Name"), max_length=128, db_index=True)

    class Meta:
        app_label = 'payment'
        ordering = ['name']
        verbose_name = _("Source Type")
        verbose_name_plural = _("Source Types")

    def __str__(self):
        return self.name


class PaymentSource(models.Model):
    """
    This model tracks the Payment sources:
    A Payment is tracked using its source type(credit card, debit card, cash, check, etc)
    And this model refers to the actual instance of the source (eg: A specific credit card, check, etc)
    """
    order = models.ForeignKey(
        'sales.CustomerOrder',
        on_delete=models.CASCADE,
        related_name='sources',
        verbose_name=_("Order"))
    source_type = models.ForeignKey(
        'payment.PaymentSourceType',
        on_delete=models.CASCADE,
        related_name="sources",
        verbose_name=_("Source Type"))
    currency = models.CharField(
        _("Currency"), max_length=12, default=settings.DEFAULT_CURRENCY)

    # Reference number for this payment source.  This is often used to look up
    # a transaction model for a particular payment partner.
    reference = models.CharField(_("Reference"), max_length=255, blank=True)

    class Meta:
        app_label = 'payment'
        ordering = ['pk']
        verbose_name = _("Source")
        verbose_name_plural = _("Sources")

    def __str__(self):
        description = _('Payment for order: %(prder)s from type %(type)s') % {
            'order': self.order,
            'type': self.source_type}
        return description


class Transaction(models.Model):
    source = models.ForeignKey(
        'payment.PaymentSource',
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name=_("Source"))

    AUTHORISE, DEBIT, REFUND = 'Authorise', 'Debit', 'Refund'
    TXN_TYPES = (
        (AUTHORISE, _("Authorized transaction")),
        (DEBIT, _("Debit")),
        (REFUND, _("Refund")),
    )
    txn_type = models.CharField(_("Type"), choices=TXN_TYPES, default=DEBIT, max_length=128, blank=True)
    amount = models.DecimalField(_("Amount"), decimal_places=2, max_digits=12)
    reference = models.CharField(_("Reference"), max_length=128, blank=True)
    status = models.CharField(_("Status"), max_length=128, blank=True)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)

    def __str__(self):
        return _("%(reference)s of %(amount).2f") % {
            'reference': self.reference,
            'amount': self.amount}

    class Meta:
        app_label = 'payment'
        ordering = ['-date_created']
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
