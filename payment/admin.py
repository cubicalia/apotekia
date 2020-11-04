from django.contrib import admin
from .models import PaymentSource, Payment, PaymentConditions
from django.contrib import admin

admin.site.register(Payment)
admin.site.register(PaymentSource)
admin.site.register(PaymentConditions)
