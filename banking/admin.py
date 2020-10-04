from django.contrib import admin
from .models import BankAccount, BaseBankEntry
from django.contrib import admin

admin.site.register(BankAccount)
admin.site.register(BaseBankEntry)
