from django.contrib import admin
from .models import InventoryLocation, InventoryTable, InventoryEntry

admin.site.register(InventoryLocation)
admin.site.register(InventoryTable)
admin.site.register(InventoryEntry)

