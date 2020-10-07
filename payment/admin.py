from django.contrib import admin
from .models import PaymentSource, PaymentSourceType, Transaction
from django.contrib import admin

admin.site.register(Transaction)
admin.site.register(PaymentSource)
admin.site.register(PaymentSourceType)