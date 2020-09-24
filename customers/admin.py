from django.contrib import admin
from .models import Customer

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class CustomerResource(resources.ModelResource):

    class Meta:
        model = Customer


class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource


admin.site.register(Customer, CustomerAdmin)
