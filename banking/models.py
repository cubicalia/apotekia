from django.db import models
from django.utils.translation import gettext_lazy as _
from apotekia.utils import get_default_currency
from apotekia import settings


class BankAccount(models.Model):
    account_name = models.CharField(_('Account Name'), max_length=20)
    # table = models.ForeignKey('inventory.InventoryTable', on_delete=models.CASCADE)
    BANK_ACCOUNT, CASH_REGISTER, SAFE = (
        "Bank Account", "Cash Register", "Safe")
    BANK_TYPES = (
        (BANK_ACCOUNT, _("Bank Account")),
        (CASH_REGISTER, _("Cash Register")),
        (SAFE, _("Safe")),
    )
    type = models.CharField(_('Account type'), choices=BANK_TYPES, default=BANK_ACCOUNT, max_length=20)
    date_opened = models.DateField(_('Date Opened'))
    account_number = models.CharField(_('Account Number'), null=True, blank=True, max_length=20)
    IBAN_number = models.CharField(_('IBAN Number'), null=True, blank=True, max_length=20)
    Swift_code = models.CharField(_('Swift CODE Number'), null=True, blank=True, max_length=20)

    initial_balance = models.DecimalField(_('Initial Balance'), decimal_places=2, max_digits=12, default=0.00)
    current_balance = models.DecimalField(_('Current Balance'), decimal_places=2, max_digits=12, default=0.00)

    class Meta:
        app_label = 'banking'
        verbose_name = _("Bank Account")
        verbose_name_plural = _("Bank Accounts")

    def __str__(self):
        return str(self.account_name) + ': ' + \
               str(self.account_number) + \
               ' contains: ' + str(self.current_balance) + ' ' + settings.DEFAULT_CURRENCY


class BaseBankEntry(models.Model):
    line_reference = models.SlugField(
        _("Line Reference"), max_length=128, db_index=True)
    account = models.ForeignKey(
        'banking.BankAccount',
        on_delete=models.CASCADE,
        related_name='lines',
        verbose_name=_("Basket"))

    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True, db_index=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True, db_index=True)

    date_of_operation = models.DateTimeField(_("Date Of Operation"), auto_now=True, db_index=True)
    date_of_value = models.DateTimeField(_("Date Of Value"), auto_now=True, db_index=True)

    value = models.DecimalField(_('Value'), decimal_places=2, max_digits=12, default=0.00)

    class Meta:
        app_label = 'banking'
        verbose_name = _("Bank Entry")
        verbose_name_plural = _("Bank Entries")

    def __str__(self):
        return str(self.line_reference) + \
               '--> ' + str(self.date_of_operation) + \
               ', account:' + str(self.account) + \
               ', amount: ' + str(self.value)


