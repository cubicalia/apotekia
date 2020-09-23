from django.contrib import admin
from .models import InventoryLocation, InventoryCustomerPurchaseExit, InventorySupplierReturnOrder

admin.site.register(InventoryLocation)
admin.site.register(InventorySupplierReturnOrder)
admin.site.register(InventoryCustomerPurchaseExit)

