from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia import settings


class PaymentSource(models.Model):
    name = models.CharField(_("Name"), max_length=128, db_index=True, unique=True)

    class Meta:
        app_label = 'payment'
        ordering = ['pk']
        verbose_name = _("Source Type")
        verbose_name_plural = _("Source Types")

    def __str__(self):
        return self.name


class PaymentConditions(models.Model):
    """
    This model informs the Payment condition of a transaction:
    """
    name = models.CharField(_("Name"), max_length=128, db_index=True, unique=True)
    description = models.TextField(_('Description'), blank=True, null=True)

    class Meta:
        app_label = 'payment'
        ordering = ['pk']
        verbose_name = _("Payment Condition")
        verbose_name_plural = _("Payment Conditions")

    def __str__(self):
        return self.name + '-' + self.description


class Payment(models.Model):
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
    date_value = models.DateTimeField(_("Date Of Value"))

    def __str__(self):
        return _("%(reference)s of %(amount).2f") % {
            'reference': self.reference,
            'amount': self.amount}

    class Meta:
        app_label = 'payment'
        ordering = ['-date_created']
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
