from __future__ import unicode_literals

from django.contrib import admin
from .models import Branch, Customer, Account, Product


admin.site.register((
    Branch,
    Customer,
    Account,
    Product
    ))

