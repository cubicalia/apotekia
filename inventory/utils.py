from apotekia import db_setup
from inventory.models import InventoryEntry, InventoryLocation, WareHouse


# We pass the product model class and expect a location
# This is used for finding allocated products over our shop/s
def find_product_locations(product):
    qs = product.inventoryentry_set.order_by('date')
    if len(qs) > 0:
        print(qs[0])
    else:
        print('No stock records for {}'.format(product.title))


