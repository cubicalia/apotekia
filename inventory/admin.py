from django.contrib import admin
from .models import InventoryLocation, InventoryEntry, StockRecord, WareHouse

admin.site.register(InventoryLocation)
admin.site.register(InventoryEntry)
admin.site.register(WareHouse)
admin.site.register(StockRecord)

