from django.contrib import admin
from .models import Product, ProductCategory, ProductImage
# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)