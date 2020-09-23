from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderLineReturn(models.Model):
    return_order = models.ForeignKey('returns.OrderReturn',
                              verbose_name=_("Order Line Returned"),
                              on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey('catalog.Product',
                                verbose_name=_("Product Returner from order"),
                                on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(_('Quantity returner of the product'))

    def __str__(self):
        return 'Product returned' + self.product.title + \
               '= ' + str(self.quantity) + ' --from order:' + self.return_order.order.number


class OrderReturn(models.Model):
    order = models.OneToOneField('sales.CustomerOrder',
                                 verbose_name=_("Return from order"),
                                 on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Items returned from order' + str(self.order.number)
