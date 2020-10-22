from django.contrib import admin
from .models import Basket, BasketLine, CustomerOrder, Sale
from django.contrib import admin

admin.site.register(BasketLine)
admin.site.register(Basket)
admin.site.register(CustomerOrder)

admin.site.register(Sale)
