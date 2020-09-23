from django.contrib import admin
from .models import OrderLineReturn, OrderReturn

admin.site.register(OrderReturn)
admin.site.register(OrderLineReturn)