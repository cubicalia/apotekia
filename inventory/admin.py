from django.contrib import admin
from .models import InventoryLocation, InventoryEntry

admin.site.register(InventoryLocation)
admin.site.register(InventoryEntry)

