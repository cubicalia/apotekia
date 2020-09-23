from django.contrib import admin
from .models import Product, ProductCategory, ProductImage
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.


class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource


admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)